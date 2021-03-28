import re
import subprocess
import sys
from pathlib import Path
from typing import Optional, Sequence

import libcst as cst
import libcst.matchers as m

LISTS_DIR = (Path.cwd() / Path(__file__)).parent / "lists"

RELEASES = {
    "2.3": "https://www.python.org/ftp/python/2.3.7/Python-2.3.7.tgz",
    "2.4": "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz",
    "2.5": "https://www.python.org/ftp/python/2.5.6/Python-2.5.6.tgz",
    "2.6": "https://www.python.org/ftp/python/2.6.9/Python-2.6.9.tgz",
    "2.7": "https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz",
    "3.0": "https://www.python.org/ftp/python/3.0.1/Python-3.0.1.tgz",
    "3.1": "https://www.python.org/ftp/python/3.1.5/Python-3.1.5.tgz",
    "3.2": "https://www.python.org/ftp/python/3.2.6/Python-3.2.6.tgz",
    "3.3": "https://www.python.org/ftp/python/3.3.7/Python-3.3.7.tgz",
    "3.4": "https://www.python.org/ftp/python/3.4.10/Python-3.4.10.tgz",
    "3.5": "https://www.python.org/ftp/python/3.5.10/Python-3.5.10.tgz",
    "3.6": "https://www.python.org/ftp/python/3.6.13/Python-3.6.13.tgz",
    "3.7": "https://www.python.org/ftp/python/3.7.10/Python-3.7.10.tgz",
    "3.8": "https://www.python.org/ftp/python/3.8.8/Python-3.8.8.tgz",
    "3.9": "https://www.python.org/ftp/python/3.9.2/Python-3.9.2.tgz",
    "3.10": "https://www.python.org/ftp/python/3.10.0/Python-3.10.0a6.tgz",
}

MODULE_DEF_RE = re.compile(r"PyModuleDef .*? = \{\s*[^,]*,\s*([^,}]+)[,}]")
MULTILINE_COMMENT_RE = re.compile(r"/\*.*?\*/")
INITTAB_RE = re.compile(r'{"([^"]+)", \S+?\}')

# lib2to3 outputs code that doesn't parse, so just omit these lines
PY2_LINES_TO_OMIT = [
    "join(F, fw + '.framework', H)",
    "for fw in 'Tcl', 'Tk'",
    "for fw in ('Tcl', 'Tk')",
    "for H in 'Headers', 'Versions/Current/PrivateHeaders'",
]


def regen_all():
    all2 = set()
    all3 = set()
    for v in RELEASES:
        names = regen(v)
        if v.startswith("2"):
            all2 |= names
        elif v.startswith("3"):
            all3 |= names
        else:
            raise ValueError("What is this brave new future you live in")

    (LISTS_DIR / "all2.txt").write_text("".join(f"{line}\n" for line in sorted(all2)))
    (LISTS_DIR / "all3.txt").write_text("".join(f"{line}\n" for line in sorted(all3)))
    (LISTS_DIR / "all.txt").write_text(
        "".join(f"{line}\n" for line in sorted(all2 | all3))
    )

    print("done")


def regen(version: str) -> Sequence[str]:
    base_path = Path(".cache", RELEASES[version].split("/")[-1].rsplit(".", 1)[0])
    setup_path = base_path / "setup.py"

    if not base_path.exists():
        Path(".cache").mkdir(exist_ok=True)
        subprocess.check_call(["wget", "-c", RELEASES[version]], cwd=".cache")
        subprocess.check_call(
            ["tar", "-xvzf", RELEASES[version].split("/")[-1]], cwd=".cache"
        )
        if version.startswith("2"):
            (base_path / "fixed").mkdir(exist_ok=True)
            subprocess.check_call(
                [
                    sys.executable,
                    "-m",
                    "lib2to3",
                    "-n",
                    "-w",
                    "-o",
                    str(base_path / "fixed"),
                    str(base_path / "setup.py"),
                ]
            )

            # TODO if the extraction succeeded but now this fails, we can end up
            # with a corrupt copy.
            setup_path = base_path / "fixed" / "setup.py"
            lines = setup_path.read_text().splitlines(True)
            lines = [line for line in lines if line.strip() not in PY2_LINES_TO_OMIT]
            setup_path.write_text("".join(lines))
    elif version.startswith("2"):
        setup_path = base_path / "fixed" / "setup.py"

    module = try_parse(setup_path)
    ev = ExtensionVisitor()
    module.visit(ev)

    # Python files
    names = ev.extension_names[:]
    for p in (base_path / "Lib").glob("*"):
        if p.name.startswith(("plat-", "lib-")):
            # 2.x platform dirs, or tk support
            for name in p.glob("*.py"):
                name = name.with_suffix("").name
                names.append(name)
        else:
            name = p.with_suffix("").name
            name = name.split(".")[0]  # __phello__.foo
            if name not in ("__pycache__", "site-packages"):
                names.append(name)

    for subdir in (
        "Python",  # builtin
        "Modules",  # other extensions, some of which are built-in :/
        "PC",  # windows
    ):
        for p in (base_path / subdir).glob("*.c"):
            try:
                data = p.read_text()
            except:
                data = p.read_text(encoding="latin-1")

            match = MODULE_DEF_RE.search(data)
            if match:
                s = MULTILINE_COMMENT_RE.sub("", match.group(1)).strip()
                if s.startswith(".m_name"):
                    s = s.split("=")[1].strip()

                if s.startswith('"') and s.endswith('"'):
                    names.append(s.strip('"'))
                elif p.name in ("_warnings.c", "_sre.c", "pyexpat.c", "_bsddb.c"):
                    names.append(p.with_suffix("").name)
                elif p.name in ("socketmodule.c", "posixmodule.c"):
                    names.append(p.name.split("module")[0])
                else:
                    print(f"Unknown module for {s} in {p}, skipped")

    # Some names are listed differently/better here; cjkcodecs and _io/io
    for path in (
        base_path / "PC" / "config.c",
        base_path / "PC" / "os2vacpp" / "config.c",
    ):
        if not path.exists():
            continue
        for match in INITTAB_RE.finditer(
            path.read_text().split("_PyImport_Inittab[] = {")[1]
        ):
            if match.group(1) == "__main__":
                continue
            names.append(match.group(1))

    # Aliases
    if version >= "3.3":
        names.append("_frozen_importlib")
    if version >= "3.5":
        names.append("_frozen_importlib_external")

    LISTS_DIR.mkdir(exist_ok=True)
    (LISTS_DIR / f"{version}.txt").write_text(
        "".join(f"{line}\n" for line in sorted(set(names)))
    )
    print(f"{version} done.")
    return set(names)


class ExtensionVisitor(cst.CSTVisitor):
    def __init__(self):
        self.extension_names = []

    def visit_Call(self, node: cst.Call) -> Optional[bool]:
        # print(node)
        d = m.extract(
            node,
            m.Call(
                func=m.Name("Extension"),
                args=(
                    m.Arg(value=m.SaveMatchedNode(m.SimpleString(), "extension_name")),
                    m.ZeroOrMore(m.DoNotCare()),
                ),
            ),
        )
        if d:
            self.extension_names.append(d["extension_name"].evaluated_value)


# This is from usort
def try_parse(path: Path, data: Optional[bytes] = None) -> cst.Module:
    """
    Attempts to parse the file with all syntax versions known by LibCST.

    If parsing fails on all supported grammar versions, then raises the parser error
    from the first/newest version attempted.
    """
    if data is None:
        data = path.read_bytes()

    parse_error: Optional[cst.ParserSyntaxError] = None

    for version in cst.KNOWN_PYTHON_VERSION_STRINGS[::-1]:
        try:
            mod = cst.parse_module(
                data, cst.PartialParserConfig(python_version=version)
            )
            return mod
        except cst.ParserSyntaxError as e:
            # keep the first error we see in case parsing fails on all versions
            if parse_error is None:
                parse_error = e

    # not caring about existing traceback here because it's not useful for parse
    # errors, and usort_path is already going to wrap it in a custom class
    raise parse_error or Exception("unknown parse failure")


if __name__ == "__main__":
    regen_all()
