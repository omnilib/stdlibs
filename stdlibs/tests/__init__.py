# Copyright 2021 John Reese
# Licensed under the MIT license

import os
import sys
from pathlib import Path
from unittest import TestCase
from unittest import mock

import stdlibs


class StdlibsTest(TestCase):
    def test_module_names(self):
        for name in ("re", "os", "sys", "posixpath", "re", "_sre", "xmlrpc"):
            self.assertIn(name, stdlibs.module_names)
        self.assertNotIn("__main__", stdlibs.module_names)

    def test_default_version(self):
        with mock.patch("stdlibs.sys.version_info", (3, 7, 5)):
            names = stdlibs.stdlib_top_level()
            self.assertEqual("<LazyFileSet 3.7.txt loaded=False>", repr(names))

    def test_api(self):
        names = stdlibs.stdlib_top_level("3.8")
        self.assertEqual("<LazyFileSet 3.8.txt loaded=False>", repr(names))
        self.assertIn("posixpath", names)
        self.assertEqual("<LazyFileSet 3.8.txt loaded=True>", repr(names))

        with self.assertRaisesRegex(
            ValueError, "foo\.bar has a dot and is not a top-level name"
        ):
            "foo.bar" in names

        t = id(names._names)
        self.assertIn("posixpath", list(names))
        # Only loads once
        self.assertEqual(t, id(names._names))
        # Error handling
        with self.assertRaisesRegex(ValueError, "No such list: 1\.0"):
            stdlibs.stdlib_top_level("1.0")

    def test_all_my_modules_are_there(self):
        # Gets only the top-level names we should have on this version
        names = stdlibs.stdlib_top_level(None)
        for module in Path(os.__file__).parent.glob("*.py"):
            name = module.with_suffix("").name
            name = name.split(".")[0]  # __phello__.foo
            if name.startswith("_sysconfigdata_"):
                continue
            self.assertIn(name, names)

    def test_all23(self):
        self.assertEqual(
            (
                set(stdlibs.stdlib_top_level("all2"))
                | set(stdlibs.stdlib_top_level("all3"))
            ),
            set(stdlibs.stdlib_top_level("all")),
        )
