stdlibs
=======

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
$ git shortlog -s 2dac1496bfe351870602bccd92da8b34d18a856b...v2021.3.25
     1	John Reese
```

