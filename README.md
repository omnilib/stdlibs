# stdlibs

Simple list of top-level packages in Python's stdlib

Note: If you only need the live module names on 3.10+, just use
`sys.stdlib_module_names`.  This is not exactly a backport, but a static list of
those for most useful Python versions.

If someone wants to add alternate runtimes, PRs welcome.


Usage
-----

Currently `stdlibs.module_names` is `stdlibs.py3.module_names` -- the top-level
names that are valid in some version of py3 on some platform.  This is a
superset of top-level names you may have, and a superset of those in
`sys.stdlib_module_names`.

```pycon
>>> from stdlibs import module_names
>>> print("os" in module_names)
True
>>> print("peg_parser" in module_names)  # 3.9+
True
```

If you need a specific version, those are available as other modules:

```pycon
>>> from stdlibs.py36 import module_names as module_names_py36
>>> print("os" in module_names)
True
>>> print("peg_parser" in module_names_py36)
False
```

If you intend to process more than one version, you may find the string api
easier:

```pycon
>>> from stdlibs import stdlib_module_names, KNOWN_VERSIONS
>>> [v for v in KNOWN_VERSIONS if "dataclasses" in stdlib_module_names(v)]
['3.7', '3.8', '3.9', '3.10']
>>>
>>> sorted(stdlib_module_names("3.7") - stdlib_module_names("3.6"))
['_abc', '_contextvars', '_py_abc', '_queue', '_uuid', '_xxtestfuzz', 'contextvars', 'dataclasses']
>>>
>>> from moreorless.click import echo_color_unified_diff
>>> prev = None
>>> for v in KNOWN_VERSIONS:
...     cur = ''.join([f"{name}\n" for name in sorted(stdlib_module_names(v))])
...     if prev:
...             echo_color_unified_diff(prev, cur, f"new-in-{v}")
...     prev = cur
--- a/new-in-2.4
+++ b/new-in-2.4
@@ -19,7 +19,6 @@
 DocXMLRPCServer
 ERRNO
 EasyDialogs
-FCNTL
 FILE
 FL
 FileDialog
<snip>
```

Install
-------

You can install it from PyPI:

```shell-session
$ pip install stdlibs
```


Regenerating
------------

If you need to regenerate the list, install libcst, add the url to
`stdlibs/fetch.py`, and run that file.  Make sure any new versions are added to
`KNOWN_VERSIONS`.


License
-------

stdlibs is copyright [John Reese](https://jreese.sh), and licensed under
the MIT license.  I am providing code in this repository to you under an open
source license.  This is my personal repository; the license you receive to
my code is from me and not from my employer. See the `LICENSE` file for details.

