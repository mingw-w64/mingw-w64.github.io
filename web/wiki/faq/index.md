# Frequently Asked Questions

## Installation

-   Q: What file should I download? / What do the names mean?
    [Answer](./download-filename-structure.md)
-   Q: How do I install the binary package in my environment?
    [Answer](./installation-of-binary-toolchain-packages.md)

## Compilation

-   Q: How do I compile the runtime?
    [Answer](./compiling-the-runtime.md)
-   Q: How do I compile Unicode Applications?
    [Answer](./unicode-apps.md)
-   Q: How do I compile multilib toolchain?
    [Answer](./multilib-toolchain.md)
-   Q: How can I check for mingw-w64 headers?
    [Answer](./check-for-mingw-w64.md)
-   Q: Why get I build failures in gcc's libstdc++ build?
    [Answer](./libstdcpp-build-failures.md)
-   Q: How can I generate an import library for a DLL?
    [Answer](./generation-of-dll-import-library.md)
-   Q: How do I use LTO (Link Time Optimization) in GCC?
    [Answer](./lto-and-gcc.md)
-   Q: How do I make use of PPL and CLooG in GCC?
    [Answer](./ppl-cloog-and-gcc.md)
-   Q: Why doesn't printf and scanf family work as defined in C99?
    [Answer](./printf-and-scanf-family.md)
-   Q: How do I compile with pthreads?
    [Answer](./compile-pthreads.md)
-   Q: Why do I get redefinition errors against winsock.h when I include
    winsock2.h?
    [Answer](./winsock2-include-order.md)
-   Q: Why doesn't mingw-w64 gcc support Dwarf-2 Exception Handling?
    [Answer](./exception-handling.md)
-   Q: How do I fix "`__mingw_aligned_malloc` not declared in this
    scope"? [Answer](./missing-_aligned_malloc.md)
-   Q: How do I use "%llu" in printf?
    [Answer](./gnu-printf.md)
-   Q: I get some errors with C++11 to\_string when building/using GCC,
    what gives? [Answer](./to_string.md)
-   Q: What are default manifest files and why do they matter?
    [Answer](./default_manifest.md)

## Execution

-   Q: Which compiler executable should I use?
    [Answer](./usable-compiler-executable.md)
-   Q: What does error 0xc000007b mean?
    [Answer](./error-0xc000007b.md)
-   Q: What does Procedure entry point XXX not located in Dynamic Link
    Library mean?
    [Answer](./procedure-entry-point.md)
-   Q: Why isn't gdb able to display symbols from DLLs?
    [Answer](./gdb-dll-symbols.md)
-   Q: Why does GDB crash with "thread.c:79: internal-error"?
    [Answer](./threadc79-internal-error.md)
-   Q: Why do some 32-bit MinGW-w64 applications fail with '...
    \_vswprintf could not be located in the dynamic link library
    msvcrt.dll'? [Answer](./_vswprintf-missing.md)
-   Q: Why crashes my 64 bit program when using a MSVC-generate x64
    \*.lib file?
    [Answer](./64-bit-msvc-generated-x64-lib.md)