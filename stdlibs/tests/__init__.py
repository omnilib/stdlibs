# Copyright 2021 John Reese
# Licensed under the MIT license

from unittest import TestCase

import stdlibs


class StdlibsTest(TestCase):
    def test_module_names(self):
        for name in ("re", "os", "sys"):
            self.assertIn(name, stdlibs.module_names)
