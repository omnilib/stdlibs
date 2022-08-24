# Copyright 2022 Amethyst Reese
# Licensed under the MIT license

"""
List of packages in the stdlib
"""

__author__ = "Amethyst Reese"

import importlib
import sys
from typing import FrozenSet, List, Optional

from . import known

from .__version__ import __version__

ALL = "all"
"""Combined 3.x and 2.x stdlibs"""

KNOWN_VERSIONS: List[str] = known.KNOWN_VERSIONS
"""All supported Python major releases"""


def stdlib_module_names(version: Optional[str] = None) -> FrozenSet[str]:
    """
    Return a set of known module names for a Python release in :data:`.KNOWN_VERSIONS`.

    If passed :data:`stdlibs.ALL`, this returns :data:`stdlibs.py.module_names`.
    If passed ``None``, or no arguments, returns the equivalent module names for the
    active major Python version.

    Prefer using :data:`stdlibs.module_names` or a specific
    :ref:`Versioned Module <versioned>` directly.
    """
    if version is None:
        version = "%d%d" % sys.version_info[:2]
        modname = f".py{version}"
    elif version == ALL:
        modname = ".py"
    else:
        version = "".join(version.split(".")[:2])
        modname = f".py{version}"

    return importlib.import_module(modname, __package__).module_names  # type: ignore


module_names: FrozenSet[str] = stdlib_module_names("3")
"""
Known stdlibs for any release of Python 3.x

Shortcut for :data:`stdlibs.py3.module_names`.
"""


__all__ = [
    "ALL",
    "KNOWN_VERSIONS",
    "module_names",
    "stdlib_module_names",
]
