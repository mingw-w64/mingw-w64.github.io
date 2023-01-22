# Feature list of mingw-w64 runtime

First we have two different target triplets, which have different
supported features. The &lt;cpu&gt;-pc-mingw32 triplet is the most
compatible configuration to mingw.org's runtime. The target triplet
&lt;cpu&gt;-w64-mingw32, introduced for gcc version 4.5.x or higher,
adds additional features to our runtime, which are supported
specifically by mingw-w64 project's runtime.  
We inherit most of the features from mingw.org's runtime including, some
parts to support POSIX extension. Additional preprocessor symbols are
required while compiling to enable those POSIX extensions.

## General differences

-   mingw-w64 supports Windows OSes starting from Windows 2000 onwards.
-   mingw-w64 runtime is not based on Cygwin's (maintained by MinGW.org)
    w32api.
-   mingw-w64 supports both x64 and x86 Windows Operating Systems.
-   mingw-w64 builds GCC, Binutils and GDB OOTB. That means no
    additional patches are necessary for build.
-   mingw-w64 provides optional SDKs for direct-x and ddk support. We
    want to thank here especially the Wine project and the ReactOS
    project for allowing us to provide it in the mingw-w64 project.
-   mingw-w64 provides optional secured C-runtime API and headers
-   mingw-w64 works with the development head of GCC and Binutils. So
    new features here are provided fast to the users of our runtime. We
    provide automated builds of the toolchains on our site.
-   mingw-w64 supports gcc's 128-bit floating point arithmetic feature.
-   mingw-w64 supports delayed load library support

## Additional features for both compatibility mode and -w64- mode

-   the mingwm10.dll is deprecated by our runtime. We did this by adding
    thread local storage callback support to our runtime. This means
    mingw-w64 is providing the support for the TLS-cleanup mechanism,
    works even for static versions of libgcc. There are no differences
    in behavior anymore.
-   the math library is adjusted to be compatible with GCC's new strict
    aliasing rules.
-   the printf-POSIX extensions are ported for new GCC's strict aliasing
    rules.
-   Headers are mostly C99 compatible.
-   Platform and runtime headers are supporting the 'no inline' feature
    of gcc.

## Additional mingw-w64 trunk version features

-   the wprintf-family POSIX extension are supported.
-   the standard math and complex math are reworked in respect to C99
    standard conformancy and runtime-speed
-   the support of new Win7/Vista API was added to platform headers.
-   the scanf/wscanf-family POSIX extension are supported.

## Additional features for configuring in -w64- mode

-   mingw-w64 supports "-municode" switch for GCC 4.5 or later . That
    means you are able to build MS style Unicode applications.
-   mingw-w64 supports optional multilib feature (see below)

## Optional features

-   multilib support for x64 default toolchains. That means you can
    build 64-bit and 32-bit programs in one environment and by the same
    compiler.