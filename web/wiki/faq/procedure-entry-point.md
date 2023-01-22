# Procedure entry point

## Procedure entry point OpenProcessToken? could not be located in the dynamic link library kernel32.dll

This error means that Windows could not resolve a symbol that it was
expecting to be exported from a DLL. There are several reasons for this.

### The symbol exists, but in a different DLL

As with different versions of Windows, exported APIs do change. To
accommodate different versions of Windows, developers can relink their
application with the link libraries specified explicitly in order. For
example, OpenProcessToken? may be found in both kernel32.dll and
advapi32.dll on Windows 7. To use the symbol from kernel32.dll, use the
link flags "-lkernel32 -ladvapi32". For the advapi32.dll copy, use
"-ladvapi32 -lkernel32" instead.

Use gcc "-v" option to see the link command in detail. Note that ld
scans the dependencies of libraries from left to right, but it will
ignore the later instances of the library if specified more than once.
It is also possible to use "-nostdlib" to link your programs, but you
must specify the startup objects manually for your program to run
properly..

### The application was built for a later or earlier version of Windows

As new APIs are introduced and deprecated APIs are removed in later
versions of Windows, your copy of Windows may not have the specified
symbol in the loaded DLL. This can be resolved by re-writing the
application to use GetProcAddress? to resolve the symbol at runtime and
gracefully handling the situation if a symbol is missing.

### Your copy of the DLL is too old or too new

As Windows is updated, some APIs may be added or removed. Check with the
application developer for more information.