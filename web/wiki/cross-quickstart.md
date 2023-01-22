# Cross Compilation Quickstart

## The Need for Cross Compilers

In a nutshell, cross compilers enable you to build applications that run
on a different type of platform than the platform you're developing on.
For example, you may wish to develop libraries on a Linux-based system
for use on a Windows-based system. Or you may wish to develop an
application on a Windows-based system for use on an ARM-based embedded
system. In both cases, it's the cross compiler that allows you to
develop and build native applications for the other platform.

The platform on which you're developing and compiling is called the
***build platform*** while the platform on which your libraries and
applications run is called the ***host platform***.

If you never build for a different host platform, there's no real need
for a cross compiler. A native compiler that builds for the same host
platform that you're developing on is really all you need to create the
next killer app.

## Cross Compiling with GNU Autotools

Compilers based upon the
<a href="http://gcc.gnu.org/" rel="nofollow">GNU Compiler Collection
(GCC)</a>, such as the ones from the MinGW-w64 project, can be built as
cross compilers or native compilers. A developer building for a
different platform simply installs (or builds) a cross compiling GCC
toolchain and any required headers and libraries. The developer then
runs a `configure` script with the appropriate `--build` and `--host`
arguments that enable the `configure` script to determine which cross
compiler to use. The `configure` script creates a customized `Makefile`
to build the binaries that run natively on the specified host platform.
Finally, the developer runs `make` to perform the build.

The values used for the `--build` and `--host` arguments are described
in more detail on the [System Type
Triplets](./type-triplets.md) page.

While the <a
href="http://www.gnu.org/software/libtool/manual/automake/GNU-Build-System.html#GNU-Build-System"
rel="nofollow">GNU Build System</a> and the `configure` script remove
much of the complexity of cross compiling, you will find source packages
in the wild that don't use a build system but still enable enable cross
compilation. For example, many source packages that have no need for the
complexity of a setting up and maintaining a build system provide a
custom `Makefile` used by both native and cross compilers. Cross
compilation support is typically provided by the `Makefile` with lines
such as

    CC := $(CROSS_COMPILE)gcc
    WINDRES := $(CROSS_COMPILE)windres
    AR := $(CROSS_COMPILE)ar
    STRIP := $(CROSS_COMPILE)strip

You may also discover `Makefile`'s that require you to explicitly set
environment variables as part of the `make` invocation to allow cross
compilation, similar to

    make -f lazy_makefile CC=i686-w64-mingw32-gcc

Other popular build systems such as
<a href="http://cmake.org" rel="nofollow">Cmake</a> and
<a href="http://waf.googlecode.com" rel="nofollow">Waf</a> also support
cross compilation.

## Cross Compilation and the MinGW-w64 Project

The MinGW-w64 project supports toolchains targeting 32 and 64-bit
systems running the Windows operating system. As the project supports
building native Windows binaries from Unix-like platforms, cross
compilation is a very important part of the MinGW-w64 project.

***TODO*** more content about the MinGW-w64 native and cross compilers

***TODO*** briefly discuss the two main perspectives; MinGW-w64 hacker
and MinGW-w64 user a la @Mook

***TODO*** add content on personal builds

## MinGW-w64 Supported Platforms

When cross compiling, MinGW-w64 toolchains support two platforms
identified with the following two type triplets. For more information on
type triplets see the [System Type
Triplets](./type-triplets.md) page.

1.  `i686-w64-mingw32` for binaries built to run on 32-bit Windows
    platforms.
2.  `x86_64-w64-mingw32` for binaries built to run on 64-bit Windows
    platforms.

## Cross Compilation Examples

The following examples should run fine on any Unix-like system with a
sane build system, but to run the examples on a Windows system you'll
need a collection of Unix tools such as `bash`, `sed`, `gawk`, `grep`,
`make`, and others. The
<a href="http://mingw.org/node/18" rel="nofollow">MSYS</a> collection
from the [MSYS SourceForge files
site](http://sourceforge.net/projects/mingw/files/MSYS/) or the
[MinGW-w64 hosted
MSYS](http://sourceforge.net/projects/mingw-w64/files/External%20binary%20packages%20%28Win64%20hosted%29/MSYS%20%2832-bit%29/)
is a convenient way to get the required tools. Once the tools are
installed, make sure they are available in you `PATH` environment
variable.

    # [Win7] configure Ruby trunk with 32bit cross compiler
    C:\ruby\build>sh -c "../configure --host=i686-w64-mingw32 --enable-shared --disable-install-doc"

***TODO*** add Linux example and GCC cross compiler example
