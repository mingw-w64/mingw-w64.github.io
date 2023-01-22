# _vswprintf missing

**Q:**  
Why do some 32-bit MinGW-w64 applications fail with '... \_vswprintf
could not be located in the dynamic link library msvcrt.dll'?

**A:**  
For C++, MinGW-w64 implements 'vswprintf (wchar\_t *stream, const
wchar\_t* format, builtin\_va\_list local\_argv)' as a call to
'\_vswprintf'. Older versions of msvcrt.dll, like the version in XP SP1,
do not include '\_vswprintf'. A workaround for this is to compile any
C++ libraries and applications that use 'vswprintf' (with the preceding
signature) with -DUSE\_MINGW\_ANSI\_STDIO.

For autotools based projects, pass
`CPPFLAGS="-D__USE_MINGW_ANSI_STDIO=1"` to configure.

For others such as the wxWidgets library for applications to be deployed
on XP SP1, build wxWidgets with the following command line:

    mingw32-make -f makefile.gcc CPPFLAGS="-D__USE_MINGW_ANSI_STDIO=1"

**Caveat:**  
`__USE_MINGW_ANSI_STDIO` means you **MUST** use C99 compliant format
placeholders, MS extensions such as `%I64d` will **NOT** work.
Alternatively, use `inttypes.h` macros instead.
