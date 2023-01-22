# Unicode applications

To compile Unicode applications, define **\_UNICODE** and **UNICODE** in
your files when compiling and add **-municode** when linking. GCC will
use the appropriate C startups for linking.

## Example

    #include <wchar.h>
    #include <stdio.h>

    int
    wmain (int argc, wchar_t **argv)
    {
      wprintf(L"Hello\n");
      return 0;
    }

While it is not necessary to define **\_UNICODE** or **UNICODE** to
compile the above code, **-municode** is needed for linking because it
uses wmain() instead of the traditional main().

    #define _UNICODE
    #define UNICODE
    #include <tchar.h>

    int
    _tmain(int argc, _TCHAR **argv)
    {
      _tprintf(__T("Hello\n"));
      return 0;
    }

The above code makes use of **tchar.h** mapping, which allows it to both
compile in Unicode and non-Unicode mode. Removing the 2 defines on top
will revert it to the traditional ANSI output. The **-municode** option
is still required when linking if Unicode mode is used.

## UNICODE and \_UNICODE

The **UNICODE** symbol is used primarily with win32 API such as those
found in **mmsystem.h** and **shellapi.h**. The **\_UNICODE** symbol is
used with headers such as **tchar.h** to direct standard C functions
such as **printf()** and **fopen()** to the Unicode versions. The
**-municode** defines **UNICODE**, but not **\_UNICODE**, it is safer to
use a macro such as bellow to ensure that Unicode functions are used
instead of their ANSI counterparts.

    #ifndef UNICODE
     #undef _UNICODE
    #else
     #ifndef _UNICODE
      #define _UNICODE
     #endif
    #endif

## C++ and wmain()

g++ doesn't know a thing about **wmain()**, therefore, marking
**wmain()** explicitly as **extern "C"** is necessary in C++ code,
otherwise linkage fails with a cryptic message of *undefined reference
to wWinMain*. Example:

    #ifndef _UNICODE
    #define _UNICODE
    #endif
    #ifndef UNICODE
    #define UNICODE
    #endif
    #include <wchar.h>
    #include <stdio.h>

    extern "C"
    int wmain(int argc, wchar_t** argv)
    {
      [... code ...]
    }

## Issues

### Help! I get an *error: unrecognized command line option "-municode"*!

Make sure you are using GCC with the vendor key "w64". To check, use
**"gcc -dumpmachine**". If it reads **x86\_64-w64-mingw32**, you are
probably using an old version of gcc that does not support this feature.
If it reads x86\_64-pc-mingw32, you will need to rebuild your toolchain
with the "w64" vendor key to enable the Unicode feature.