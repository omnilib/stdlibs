# Copyright 2021 John Reese
# Licensed under the MIT license

"""
List of packages in the stdlib
"""

__author__ = "John Reese"

import pkgutil
import sys
from typing import FrozenSet, Optional

from .__version__ import __version__

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
    "all",
    "all2",
    "all3",
]


class LazyFileSet:
    _names: Optional[FrozenSet[str]] = None

    def __init__(self, filename: str):
        if filename[:-4] not in KNOWN_VERSIONS:
            raise ValueError(f"No such list: {filename}")
        self.filename = filename

    def _load(self):
        if self._names is None:
            self._names = frozenset(
                pkgutil.get_data("stdlibs", f"lists/{self.filename}")
                .decode()
                .splitlines()
            )

    def __contains__(self, x):
        if "." in x:
            raise ValueError(f"{x} has a dot and is not a top-level name")
        self._load()
        return x in self._names

    def __iter__(self):
        self._load()
        return iter(self._names)

    def __repr__(self) -> str:
        return f"<LazyFileSet {self.filename} loaded={self._names is not None}>"


def stdlib_top_level(version: Optional[str] = None):
    if version is None:
        version = "%d.%d" % sys.version_info[:2]
        return LazyFileSet(f"{version}.txt")
    elif version == ALL:
        return LazyFileSet("all.txt")
    else:
        version = ".".join(version.split(".")[:2])
        return LazyFileSet(f"{version}.txt")


module_names = stdlib_top_level("all3")

__all__ = [
    "stdlib_top_level",
    "module_names",
]
