# Usable compiler executable

After installing a MinGW-w64 based toolchain, one often explores their
installation directory (**`prefix`** for this answer) and discovers
multiple versions of the same build tool living in different locations.
Which version should be used?

## Short Answer

**Always** use the executables found in the immediate `bin` subdirectory
of the installation directory, i.e. the executables living in
`<prefix>/bin`.

## Long Answer

Depending upon your system and how the MinGW-w64 toolchain was built,
you'll discover build tools living in `<prefix>/bin` and
`<prefix>/<target-alias>/bin`. For example, on a Windows 64bit machine
using one of the pre-built 64bit toolchains, executables live in
`<prefix>/bin` and `<prefix>/x86_64-w64-mingw32/bin`. Use **only** the
executables in `<prefix>/bin`. The executables in `<prefix>/bin` are
meant to be directly invoked by developers building software with the
toolchain. The executables living in `<prefix>/<target-alias>/bin` are
used internally by the build tools and **must never be directly
invoked**.

Repeat after me: *I will **never** directly invoke the executables
living in `<prefix>/<target-alias>/bin`*.

A related issue is build tool naming. Depending upon how your toolchain
was built, you may find both *prefixed* and *non-prefixed* versions of
tools in `<prefix>/bin` for the `gcc` compiler driver and other tools.
For example, on my Windows 64bit machine with a pre-built 64bit
toolchain, both `gcc.exe` and `x86_64-w64-mingw32-gcc.exe` exist in
`<prefix>/bin`. Which one should be invoked? While it is perfectly
acceptable to directly invoke `x86_64-w64-mingw32-gcc.exe`, unless you
are [cross compiling](../cross-quickstart.md) (the reason
why build tool executables use the prefixed name convention) it is often
more convenient to invoke the non-prefixed `gcc.exe`. The same advice
goes for other executables living in `<prefix>/bin`.

If your particular toolchain provides only prefixed executables in
`<prefix>/bin`, it is acceptable to directly invoke those executables.
Often, those who find the prefixed executable names living in
`<prefix>/bin` too verbose simply create more conveniently named
symlinks or renamed copies of the original executable.
