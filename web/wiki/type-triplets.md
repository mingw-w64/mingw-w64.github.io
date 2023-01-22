# System Type Triplets

## The Need for System Identification

As mentioned in [Cross Compilation Quickstart](./cross-quickstart.md), the Autotools
generated `configure` script used to simplify cross compilation creates
a `Makefile` customized to your platform and development needs. The
`configure` script tries it's best to figure out what to do, in part, by
working with it's friends `config.guess` and `config.sub` to guess your
platform type.

While the whole process is rather clever and tends to work automagically
in many cases, there are situations such as cross compiling where you
need to help `configure` by explicitly identifying your system type. You
identify your system type by setting `configure`'s `--build`, `--host`,
and (sometimes) `--target` arguments to the correct ***target triplet***
values.

## Target Triplets and the Configure Script

The ***target triplet*** has the form *cpu-vendor-os* where *os* can
take the form of *system* or *kernel-system*. The three command line
`configure` options used to specify system type are:

--build=*type*

> the type of the system used to configure and build the package.
> Defaults to output of `config.guess`.

--host=*type*

> the type of the system on which the built package executes. Defaults
> to the same type as the build system and enables cross compilation
> mode.

--target=*type*

> used for building compiler tools for cross compiling. The type of the
> system for which any compiler tools built from the package produce
> code for. Defaults to the same type as the host.

To see what `configure` thinks is the triplet for your build system,
simply execute the `config.guess` script from any source package you may
have extracted to your system. For example, on my Windows 7 32-bit
Ultimate system with a
<a href="http://mingw.org/node/18" rel="nofollow">MSYS Unix-like shell
environment</a> installed, the `configure` used by `libxml2`, by
default, will identify my build system as `i686-pc-mingw32`.

    C:\Users\Jon\Documents\libxml2-2.7.8>sh -c "./config.guess"
    i686-pc-mingw32

If you do need to override `config.guess`, provide a value to
`configure`'s `--build` argument not `--host` since using `--host` will
cause `configure` to enter cross compilation mode.

In many cases `configure` can recognize short aliases for common system
type triplets as `configure` uses the `config.sub` helper script to
canonicalize system type aliases. To see the canonical triplet for a
given alias, try something similar to

    C:\Users\Jon\Documents>sh -c "./config.sub xbox"
    i686-pc-mingw32

    C:\Users\Jon\Documents>sh -c "./config.sub mingw32"
    i386-pc-mingw32

    C:\Users\Jon\Documents>sh -c "./config.sub mac"
    m68k-apple-macos

## Triplets and MinGW-w64

When using the MinGW-w64 cross compilers, while you may need to use
different `--build` triplets, you will only use the `--host` triplets
`i686-w64-mingw32` or `x86_64-w64-mingw32`. Use `i686-w64-mingw32` when
building for 32-bit Windows platforms, and `x86_64-w64-mingw32` when
building for 64-bit Windows platforms. When using the MinGW-w64 native
compilers, you typically do not need to provide `configure` any type
triplet information .
