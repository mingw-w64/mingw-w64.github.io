# Compiling the Runtime

Building the MinGW runtime for x86\_64 is fairly straightforward, though
there are several options available to give flexibility to the build.
For the package itself, options are still being added and removed as
development progresses. That said, this space should be relatively up to
date.

After extracting the source distribution package, you will have a
directory structure containing all of the source files and configuration
files. Of particular import is the configure script. Like most projects,
mingw-w64 uses autoconf and automake to ease building. Autoconf is what
builds the configure script, which is distributed in the package. If you
want to edit the configure script, instead edit configure.ac and rerun
autoreconf to rebuild configure.

Currently, configure supports the following options:

### --build=triplet

### --host=triplet

These options set the build and host triplets. If you are building a
complete gcc toolchain, the "target" of gcc and binutils becomes the
"host" of the runtime. The "host" of gcc and binutils likewise becomes
the "build" of the runtime. The "target" option is not available for the
runtime, as it has no meaning. Similarly, "build" for binutils and gcc
is dropped for the runtime. This table may help in understanding:

===This option in gcc/binutils...===  
===...Becomes this option in the runtime===

--build  
dropped

--host  
--build

--target  
--host

### --enable-lib32

### --disable-lib32

This option, disabled by default, will enable lib32 support in the
runtime. It will result in compiling everything under /lib32, and will
allow generating binaries for 32-bit windows.

### --disable-lib64

### --enable-lib64

This option, enabled by default, will enable lib64 support in the
runtime. It will result in compiling everything under /lib64, and will
allow generating binaries for 64-bit windows.

Note: If both lib32 and lib64 are enabled, it will result in a compiler
that supports multilib. That is, one compiler can generate code for both
32-bit windows as well as 64-bit windows.