# Installation of binary toolchain packages

This page describes the installation of binaries found on the
sourceforge downloads page. Your vendor may have already packaged
similar binaries for your distribution, for instructions on installing
vendor provided binaries, please consult your distribution
documentation.

The install procedures for the downloaded binaries (*.tar.bz2 or* .zip)
are nearly similar for different platforms. Please note that ONLY the
TOP LEVEL "bin" directory executables should be used, the binaries in
the deeper directories are for GCC support and not for use by the user.

## Installation in linux environment

Extract the toolchain tarball within a folder of your choice, e.g.
~mingw\_w64. Add to your PATH environment variable the path to the bin
directory in the toolchain package, e.g. ~mingw\_w64/bin.

## Installation in cygwin environment

Extract the toolchain tarball within a folder of your choice, e.g.
~mingw\_w64. Add to your PATH environment variable the path to the bin
directory in the toolchain package, e.g. ~mingw\_w64/bin.

## Installation in msys environment

Extract the toolchain tarball/zip archive within a folder of your
choice, e.g. c:\\mingw\_w64. Add to your PATH environment variable the
path to the bin directory in the toolchain package, e.g.
c:\\mingw\_w64\\bin.

## Installation on native environment

Extract the toolchain tarball/zip archive within a folder of your
choice, e.g. c:\\mingw\_w64. Open a command shell and add to your PATH
environment variable the path to the bin directory in the toolchain
package, e.g. c:\\mingw\_w64\\bin.

## Important notice for gcc 4.6.0 (and newer) based Cross Compiler toolchains

For gcc version 4.6.0 (&gt;= 26th January 2011) or newer toolchains, the
runtime DLL libraries are no longer placed into the top level bin
directory. Instead you will find them in the system's root
&lt;target&gt;/lib folder.

To run compiled programs on the host machine (eg with wine, MSYS or
Cygwin), make sure to edit your PATH environment appropriately so the
DLLs are found by the compiled programs.