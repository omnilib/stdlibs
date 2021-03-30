# Copyright 2021 John Reese
# Licensed under the MIT license

"""
List of packages in the stdlib
"""

__author__ = "John Reese"

import importlib
import sys
from typing import FrozenSet, Optional

from .__version__ import __version__
from .py3 import module_names

ALL = "all"

KNOWN_VERSIONS = [
    "2.3",
    "2.4",
    "2.5",
    "2.6",
    "2.7",
    "3.0",
    "3.1",
    "3.2",
    "3.3",
    "3.4",
    "3.5",
    "3.6",
    "3.7",
    "3.8",
    "3.9",
    "3.10",
]


def stdlib_module_names(version: Optional[str] = None) -> FrozenSet[str]:
    if version is None:
        version = "%d%d" % sys.version_info[:2]
        modname = f".py{version}"
    elif version == ALL:
        modname = ".py"
    else:
        version = "".join(version.split(".")[:2])
        modname = f".py{version}"

    return importlib.import_module(modname, __package__).module_names  # type: ignore


__all__ = [
    "stdlib_module_names",
    "module_names",
]
