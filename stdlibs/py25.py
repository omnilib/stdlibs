# Copyright 2021 John Reese
# Licensed under the MIT license

# Generated by stdlibs/fetch.py

module_names = frozenset(
    [
        "AL",
        "Audio_mac",
        "BaseHTTPServer",
        "Bastion",
        "CD",
        "CDIO",
        "CDROM",
        "CGIHTTPServer",
        "CL",
        "CL_old",
        "Canvas",
        "Carbon",
        "ColorPicker",
        "ConfigParser",
        "Cookie",
        "DEVICE",
        "DLFCN",
        "Dialog",
        "DocXMLRPCServer",
        "ERRNO",
        "EasyDialogs",
        "FILE",
        "FL",
        "FileDialog",
        "FixTk",
        "FrameWork",
        "GET",
        "GL",
        "GLWS",
        "HTMLParser",
        "IN",
        "IOCTL",
        "MacOS",
        "MimeWriter",
        "MiniAEFrame",
        "Nav",
        "OSATerminology",
        "PixMapWrapper",
        "Queue",
        "SOCKET",
        "STROPTS",
        "SUNAUDIODEV",
        "SV",
        "ScrolledText",
        "SimpleDialog",
        "SimpleHTTPServer",
        "SimpleXMLRPCServer",
        "SocketServer",
        "StringIO",
        "TYPES",
        "Tix",
        "Tkconstants",
        "Tkdnd",
        "Tkinter",
        "UserDict",
        "UserList",
        "UserString",
        "WAIT",
        "_AE",
        "_AH",
        "_App",
        "_CF",
        "_CG",
        "_CarbonEvt",
        "_Cm",
        "_Ctl",
        "_Dlg",
        "_Drag",
        "_Evt",
        "_File",
        "_Fm",
        "_Folder",
        "_Help",
        "_IBCarbon",
        "_Icn",
        "_LWPCookieJar",
        "_Launch",
        "_List",
        "_Menu",
        "_Mlte",
        "_MozillaCookieJar",
        "_OSA",
        "_Qd",
        "_Qdoffs",
        "_Qt",
        "_Res",
        "_Scrap",
        "_Snd",
        "_TE",
        "_Win",
        "__builtin__",
        "__future__",
        "__hello__",
        "__phello__",
        "_ast",
        "_bisect",
        "_bsddb",
        "_codecs",
        "_codecs_cn",
        "_codecs_hk",
        "_codecs_iso2022",
        "_codecs_jp",
        "_codecs_kr",
        "_codecs_tw",
        "_csv",
        "_ctypes",
        "_ctypes_test",
        "_curses",
        "_curses_panel",
        "_elementtree",
        "_emx_link",
        "_functools",
        "_hashlib",
        "_heapq",
        "_hotshot",
        "_locale",
        "_lsprof",
        "_md5",
        "_msi",
        "_multibytecodec",
        "_random",
        "_sha",
        "_sha256",
        "_sha512",
        "_socket",
        "_sqlite3",
        "_sre",
        "_ssl",
        "_strptime",
        "_struct",
        "_subprocess",
        "_symtable",
        "_testcapi",
        "_threading_local",
        "_tkinter",
        "_types",
        "_weakref",
        "_winreg",
        "aepack",
        "aetools",
        "aetypes",
        "aifc",
        "al",
        "anydbm",
        "applesingle",
        "appletrawmain",
        "appletrunner",
        "argvemulator",
        "array",
        "asynchat",
        "asyncore",
        "atexit",
        "audiodev",
        "audioop",
        "autoGIL",
        "base64",
        "bdb",
        "bgenlocations",
        "binascii",
        "binhex",
        "bisect",
        "bsddb",
        "bsddb185",
        "buildtools",
        "bundlebuilder",
        "bz2",
        "cPickle",
        "cProfile",
        "cStringIO",
        "calendar",
        "cd",
        "cddb",
        "cdplayer",
        "cfmfile",
        "cgi",
        "cgitb",
        "chunk",
        "cl",
        "cmath",
        "cmd",
        "code",
        "codecs",
        "codeop",
        "collections",
        "colorsys",
        "commands",
        "compileall",
        "compiler",
        "contextlib",
        "cookielib",
        "copy",
        "copy_reg",
        "crypt",
        "csv",
        "ctypes",
        "curses",
        "datetime",
        "dbhash",
        "dbm",
        "decimal",
        "difflib",
        "dircache",
        "dis",
        "distutils",
        "dl",
        "doctest",
        "dumbdbm",
        "dummy_thread",
        "dummy_threading",
        "email",
        "encodings",
        "errno",
        "exceptions",
        "fcntl",
        "filecmp",
        "fileinput",
        "findertools",
        "fl",
        "flp",
        "fm",
        "fnmatch",
        "formatter",
        "fpectl",
        "fpetest",
        "fpformat",
        "ftplib",
        "functools",
        "gc",
        "gdbm",
        "gensuitemodule",
        "gestalt",
        "getopt",
        "getpass",
        "gettext",
        "gl",
        "glob",
        "gopherlib",
        "grp",
        "gzip",
        "hashlib",
        "heapq",
        "hmac",
        "hotshot",
        "htmlentitydefs",
        "htmllib",
        "httplib",
        "ic",
        "icglue",
        "icopen",
        "idlelib",
        "ihooks",
        "imageop",
        "imaplib",
        "imgfile",
        "imghdr",
        "imp",
        "imputil",
        "inspect",
        "itertools",
        "jpeg",
        "keyword",
        "linecache",
        "linuxaudiodev",
        "locale",
        "logging",
        "macerrors",
        "macfs",
        "macostools",
        "macpath",
        "macresource",
        "macurl2path",
        "mailbox",
        "mailcap",
        "markupbase",
        "marshal",
        "math",
        "md5",
        "mhlib",
        "mimetools",
        "mimetypes",
        "mimify",
        "mmap",
        "modulefinder",
        "msilib",
        "msvcrt",
        "multifile",
        "mutex",
        "netrc",
        "new",
        "nis",
        "nntplib",
        "nt",
        "ntpath",
        "nturl2path",
        "opcode",
        "operator",
        "optparse",
        "os",
        "os2",
        "os2emxpath",
        "ossaudiodev",
        "panel",
        "panelparser",
        "parser",
        "pcre",
        "pdb",
        "pickle",
        "pickletools",
        "pimp",
        "pipes",
        "pkgutil",
        "platform",
        "plistlib",
        "popen2",
        "poplib",
        "posix",
        "posixfile",
        "posixpath",
        "pprint",
        "profile",
        "pstats",
        "pty",
        "pure",
        "pwd",
        "py_compile",
        "pyclbr",
        "pydoc",
        "pyexpat",
        "quopri",
        "random",
        "re",
        "readcd",
        "readline",
        "repr",
        "resource",
        "rexec",
        "rfc822",
        "rgbimg",
        "riscosenviron",
        "riscospath",
        "rlcompleter",
        "robotparser",
        "rourl2path",
        "runpy",
        "sched",
        "select",
        "sets",
        "sgi",
        "sgmllib",
        "sha",
        "shelve",
        "shlex",
        "shutil",
        "signal",
        "site",
        "smtpd",
        "smtplib",
        "sndhdr",
        "socket",
        "spwd",
        "sqlite3",
        "sre",
        "sre_compile",
        "sre_constants",
        "sre_parse",
        "stat",
        "statvfs",
        "string",
        "stringold",
        "stringprep",
        "strop",
        "struct",
        "subprocess",
        "sunau",
        "sunaudio",
        "sunaudiodev",
        "sv",
        "symbol",
        "symtable",
        "sys",
        "syslog",
        "tabnanny",
        "tarfile",
        "telnetlib",
        "tempfile",
        "terminalcommand",
        "termios",
        "textwrap",
        "this",
        "thread",
        "threading",
        "time",
        "timeit",
        "timing",
        "tkColorChooser",
        "tkCommonDialog",
        "tkFileDialog",
        "tkFont",
        "tkMessageBox",
        "tkSimpleDialog",
        "toaiff",
        "token",
        "tokenize",
        "torgb",
        "trace",
        "traceback",
        "tty",
        "turtle",
        "types",
        "unicodedata",
        "unittest",
        "urllib",
        "urllib2",
        "urlparse",
        "user",
        "uu",
        "uuid",
        "videoreader",
        "warnings",
        "wave",
        "weakref",
        "webbrowser",
        "whichdb",
        "winsound",
        "wsgiref",
        "xdrlib",
        "xml",
        "xmllib",
        "xmlrpclib",
        "xx",
        "xxsubtype",
        "zipfile",
        "zipimport",
        "zlib",
    ]
)
