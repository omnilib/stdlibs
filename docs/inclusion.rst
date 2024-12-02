Name Inclusion
==============

This project lists top-level names that are likely to work as imports in an
out-of-the-box Python interpreter.  It is a superset of what you find in
``sys.stdlib_module_names`` on a modern version, but we give consistent answers
regardless of the version of python you're running, the platform, availability
of native libs, or compile args.

We haven't seen a compelling reason to add code to:

* special-case test names other than the top-level "test"
* handle sub-modules
* include names that only existed for prerelease, after a final is out
* use any finer granularity than *major*.*minor* [and in fact, the simplest use is just *major*]

The intended audience is people writing tools that need to understand imports,
such as import sorters or dependency checkers, to be able to know which names
are plausibly stdlib.

We intentionally take the union of names available across versions and
platforms, and don't sweat the exact import name -- being more precise in those
directions leads to complex code.  If you find you have different needs, see
the source for `generate_stdlib_module_names.py`_ or the discussion on `issue 127484`_.

.. _generate_stdlib_module_names.py: https://github.com/python/cpython/blob/main/Tools/build/generate_stdlib_module_names.py
.. _issue 127484: https://github.com/python/cpython/issues/127484
