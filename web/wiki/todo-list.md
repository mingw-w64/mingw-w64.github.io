# TODO List

## MinGW-w64 TODO List

Sometimes it's helpful to keep a list of things somewhere that you need
to do. If you want to work on any of these areas, jump in head first.

-   GMP supports Win64 since version 5.0.0 (version 4.3.2 also supports
    win64 with an extra patch), however no x64 asm is there yet.
-   gdb -- Native support is present, but some features like multi-arch
    support (debugging 32-bit and 64-bit by one gdb) are still missing
    features.
-   Complete the directx 8, 9 & 10 support.
-   The configure and build system should get easier for building our
    toolchain. We plan before final release major improvements about our
    make system, so that less manual configure steps are necessary.
-   Integrating of POSIX-pthread library into standard runtime. First
    implementation for it can be found in our experimental tree in the
    winpthread-directory.
-   Generation of MIDL/WIDL headers out of IDL files in maintainer-mode.
-   Add runtime-function emulation for API - like \_wsopen\_s,
    \_sopen\_s, etc - not provided in older msvcrt.dll versions.

## Bug Hunting

-   Remove 'exec' warnings everywhere
-   Handle all the many pointer/integer casting issues when compiling
    gcc for the native toolchain
-   ICEs in testsuite -- make list here? Make a separate Wiki-page out
    of that IMHO

## Documentation

-   Test howto's that are listed on the [main
    page](./home.md), update them or provide feedback.
-   Create more howto's, possibly for specific builds and/or usage
    examples.

## Done TODO

-   gdb -- Support is on gdb's mainline present. Win64 gdbserver support
    is present since version 7.1.50-20100420-cvs. We still provide our
    experimental version, but everybody can build it now from gdb's
    project sources, too. Thanks to the gdb team for supporting our
    target.
-   Fixed stack probing so that g++/iostream works
-   DDK support for 32-bit and 64-bit Windows OSes. Thanks to ReactOS
    team for allowing us to use their DDK header-set.

## TODOs planned for binutils

-   Cleanup binutils coff support and merge shared functionallity into
    bfd.
-   Improve generated import libraries by binutils so that they can be
    used as input by VC, too.
-   Support .def files directly as descriptor of import library for ld.

## Done TODO for binutils

-   Support of linking multiple resource object files compiled with
    windres to an executable (2.23.51 and newer).
-   Fix architecture detection for windmc tool for arm wince target.
    (2.20.51 and newer)
-   Add automated fixup of stdcall/fastcall functions for
    --enable-stdcall-fixup option by direct imports without decoration.
    (2.20.51 and newer)
-   Improve dllwrap tool so that it supports x64 architecture proper,
    too. (2.20.51 and newer)
-   Cleanup ld's entry-point handling for pe-coff targets and default
    for shared and dll linking to their dll-entry-point default. By this
    feature it isn't necessary to specify for shared and dll linking the
    entry point, when the default one is used. (2.20.51 and newer)
-   Correct behavior of base-file option, so that section-relative
    relocations don't lead to image-based relocations (well known issue
    about non-working rebased executables with debug-information).
-   Change underscoring behavior of binutils for w64 target and add
    command-line switches for fallback to current underscoring behavior
    (In progress: -(no-)leading-underscore option added to binutils'
    tools).
-   Support new object file format by MS in bfd as input.
-   Fix and unify name decoration in binutils. There is also an hic-up
    about fastcall decoration.

## TODOs planned for gcc

-   Append GCC Major and Minor version to GCC dlls for Windows targets
    (e.g. libgcc\_s\_4.6.dll, cygstdc++-6\_4.6.dll)
-   Improve support of msvcrXX runtimes.
-   Help provide GCC with Structured Exception Handling (SEH) support:

<a href="http://gcc.gnu.org/wiki/WindowsGCCImprovements"
rel="nofollow">http://gcc.gnu.org/wiki/WindowsGCCImprovements</a>

-   Determine where to install the libraries. There is discussion about
    this on the mailing list and on the forum. Basically, the FHS says
    to put 64-bit libraries in /lib64 and 32-bit libraries in /lib. gcc
    only looks in /lib for the mingw32 target, so to change this for
    x86\_64-pc-mingw32 requires work on the gcc end. Currently, we put
    everything into $(prefix)/$(target)/lib, but this causes issues when
    building the 32-bit libraries alongside the 64-bit libraries for a
    multilib configuration. Basically, I think that we need someone to
    modify gcc to support /lib64, and put all 64-bit libraries in
    $(prefix)/$(target)/lib64
-   To compound the above issue, there is contention over where to have
    the sysroot files. Most gcc targets look in $sysroot/usr/local by
    default. The MinGW project modified gcc to look in $sysroot/mingw by
    default. However, binutils and gcc install things into
    $sysroot/$target by deafult. So far, we are kludging around this
    issue by making $sysroot/mingw and symlink pointing to
    $sysroot/target, but we really should find a better way to handle
    the file system of the toolchain. It shouldn't be this complicated.
    More accurately, there should be a defined reference somewhere on
    the 'net that *standardizes* where stuff should be. (will be done
    for 4.8)

## Done TODOs for gcc

-   Add support of \_ int128 types as native (done for 4.6).
-   Change default underscoring of x64 Windows target (done for 4.6).
-   Move push\_macro/pop\_macro feature from gcc into libcpp, so that it
    can be used in g++ and cpp, too. (done for 4.4.3 and newer).
-   Support thiscall calling convention for x86 targets.
-   Add SEH2 function prologue generation of x64 Windows (preparing
    patches for gcc and binutils).
-   Support of multilib build in configure and in gcc. Parts are already
    present in gcc's 4.5 version by using target triplet
    &lt;cpu&gt;-w64-mingw32.
-   Port of libjava for x64 Windows (mainly done for 4.7 - just one
    hic-up about libtool-library-handling).
-   Enable the use of shared Obj-C and Std-C++ libraries (at the moment
    they aren't build, because libtool checks for 64-bit mingw for wrong
    patterns).
-   Support of -municode switch for gcc (already present for gcc's 4.5
    version by using target triplet &lt;cpu&gt;-w64-mingw32)
