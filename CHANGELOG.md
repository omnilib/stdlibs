stdlibs
=======

v2022.3.16
----------

Maintenance release

* Updated fetch script to generate docs
* Generated doc site using Sphinx and RTD
* Improved readme overview
* Ownership tranferred to Omnilib Project

```
$ git shortlog -s v2022.2.2...v2022.3.16
     7	John Reese
     6	dependabot[bot]
```


v2022.2.2
---------

Feature release

- Added stdlibs for 3.11 (#6)
- Updated release URLs (#5)

```
$ git shortlog -s v2021.4.1...v2022.2.2
     8	John Reese
     3	Tim Hatch
```


v2021.4.1
---------

Bugfix release

* Remove "test" module from py2x stdlibs (#4)
* Fix documentation and run doctest on README (#3)

```
$ git shortlog -s v2021.3.30...v2021.4.1
     3	John Reese
     2	Tim Hatch
```


v2021.3.30
----------

Feature release

* Use generated submodules of each major Python version back to 2.3 (#1)
* Default to listing all known module names from all Python 3.x versions (#1)
* Remove unnecessary runtime dependencies (#2)

```
$ git shortlog -s v2021.3.25...v2021.3.30
     5	John Reese
     8	Tim Hatch
```


v2021.3.25
----------

Initial release

* `module_names` is just `sys.stdlib_module_names` from 3.10
* That's it. That's the package.

```
$ git shortlog -s v2021.3.25
     5	John Reese
```

