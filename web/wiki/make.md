# Make

## The mingw-w64/w32 package

This is a binary package for GNU Make, patched for use with
mingw-w64/w32. It contains 32 and 64-bit executables and has three
identical files for each. They only differ by name, and this is to suit
everyone needing a particular convention:

-   make.exe: traditional name for GNU Make on popular linux
    distributions. This will conflict (badly) with MSYS Make
-   gmake.exe: another common name for GNU Make, does not conflict with
    MSYS Make.
-   mingw32-make: name thought up by mingw.org to distinguish the win32
    variant of GNU Make. This name will be required by several software
    packages: Qt, CMake...

These three can coexist in a same directory, with make.exe being the
only troublesome one which cannot be present when using MSYS.

## Installation

Just copy any of the \*make.exe files to &lt;mingw64&gt;\\bin and you're
good to go.
