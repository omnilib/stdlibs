# Copyright 2021 John Reese
# Licensed under the MIT license

import os
import sys
from pathlib import Path
from unittest import mock, TestCase

import stdlibs


class StdlibsTest(TestCase):
    def test_module_names(self) -> None:
        for name in ("re", "os", "sys", "posixpath", "re", "_sre", "xmlrpc"):
            self.assertIn(name, stdlibs.module_names)
        self.assertNotIn("__main__", stdlibs.module_names)

    def test_default_version(self) -> None:
        with mock.patch("stdlibs.sys.version_info", (3, 7, 5)):
            names = stdlibs.stdlib_module_names()
        self.assertEqual(names, stdlibs.stdlib_module_names("3.7"))

    def test_api(self) -> None:
        names = stdlibs.stdlib_module_names("3.8")
        self.assertIn("posixpath", names)

        # Error handling
        with self.assertRaises(ImportError):
            stdlibs.stdlib_module_names("1.0")

    def test_all_my_modules_are_there(self) -> None:
        # Gets only the top-level names we should have on this version
        names = stdlibs.stdlib_module_names(None)
        for module in Path(os.__file__).parent.glob("*.py"):
            name = module.with_suffix("").name
            name = name.split(".")[0]  # __phello__.foo
            if name.startswith("_sysconfigdata_"):
                continue
            self.assertIn(name, names)

    def test_all23(self) -> None:
        self.assertEqual(
            stdlibs.stdlib_module_names("2") | stdlibs.stdlib_module_names("3"),
            stdlibs.stdlib_module_names("all"),
        )

    def test_readme_example(self) -> None:
        self.assertEqual(
            ["3.7", "3.8", "3.9", "3.10", "3.11"],
            [
                v
                for v in stdlibs.KNOWN_VERSIONS
                if "dataclasses" in stdlibs.stdlib_module_names(v)
            ],
        )
