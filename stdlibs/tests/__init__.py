# Copyright 2022 Amethyst Reese
# Licensed under the MIT license

import doctest
import os
import sys
from pathlib import Path
from unittest import mock, skipIf, TestCase, TestLoader, TestSuite

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

    @skipIf(
        not hasattr(sys, "stdlib_module_names"), "sys.stdlib_module_names not present"
    )
    def test_sys_stdlib_modules_agrees(self) -> None:
        names = stdlibs.stdlib_module_names(None)
        self.assertEqual(frozenset(), sys.stdlib_module_names - names)  # type: ignore

    def test_all23(self) -> None:
        self.assertEqual(
            stdlibs.stdlib_module_names("2") | stdlibs.stdlib_module_names("3"),
            stdlibs.stdlib_module_names("all"),
        )


def load_tests(loader: TestLoader, tests: TestSuite, _pattern: None) -> TestSuite:
    tests.addTests(doctest.DocFileSuite("../../README.md"))
    return tests
