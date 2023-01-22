# General Usage Instructions

## Downloading the toolchain

There are several options you can choose from:

-   rubenvb "release" builds: these are stable builds using the latest
    released GCC and MinGW-w64. GCC 4.5 and up is covered, along with
    packages for Clang 3.1 and up. Some experimental and unstable
    packages are also provided for those that want prerelease versions
    of the software.
    -   [64-bit
        target](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/rubenvb/)
    -   [32-bit
        target](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/rubenvb/)

> > The prefix i686=32-bit x86\_64=64-bit shows what kind of binaries
> > the toolchain builds. The suffix shows what OS the toolchain is
> > built for. If you need to build 32-bit binaries on Windows, it is
> > recommended to use the i686...win32 package.

-   [MinGW-builds](https://sourceforge.net/projects/mingwbuilds/): high
    quality toolchains, providing dual-target builds(host=x32 -&gt;
    target=x32/x64 & host=x64 -&gt; target=x64/x32). GCC 4.6.2 and up is
    covered. The builds are divided into two categories:
    [stable](https://sourceforge.net/projects/mingwbuilds/files/host-windows/releases/)
    and
    [unstable](https://sourceforge.net/projects/mingwbuilds/files/host-windows/testing/).
    Also, the builds provide two models of threads: posix/win32. In
    addition to this, you can select dwarf/sjlj/seh builds at your
    choice. And one more important feature of the builds is that the
    builds include python interpreter built within the MinGW-builds
    project, and which is used for the 'GDB pretty-printers'. Also
    provides other useful packages.
    -   [64-bit
        target](https://sourceforge.net/projects/mingwbuilds/files/host-windows/releases/4.8.0/64-bit/)
    -   [32-bit
        target](https://sourceforge.net/projects/mingwbuilds/files/host-windows/releases/4.8.0/32-bit/)

> > The prefix x32=32-bit x64=64-bit shows what kind of binaries the
> > toolchain builds. If you need to build 32-bit binaries on Windows,
> > it is recommended to use the x32 package.

-   Automated builds: produced regularly, as often as possible. These
    will use upstream GCC versions and may not be very stable at times,
    but these are tested to at least function. The binary packages do
    not include optional mingw-w64 SDKs, including the DXSDK and DDK.
    -   [64-bit
        target](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Automated%20Builds/)
    -   [32-bit
        target](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Automated%20Builds/)
-   <a href="http://tdm-gcc.tdragon.net/" rel="nofollow">TDM-GCC</a>:
    TDM, who also catered updated GCC installers for mingw.org, supports
    a mingw-w64 toolchain. Be sure to read the Getting Started page.
    This is of course not usable for cross-compilation. Please
    understand TDM uses nonstandard patching that makes his builds
    binary incompatible with all other builds without these patches.

For linux, see below.

## Installing the toolchain

### Windows native

TDM-GCC comes with an easy installer, please use that. The other builds
are quite straightforward to set up:

-   extract the toolchain to a directory: 32-bit mingw-w32: eg
    `C:\mingw32` so that `C:\mingw32\bin` contains
    i686-w64-mingw32-gcc.exe 64-bit mingw-w64: eg `C:\mingw64` so that
    `C:\mingw64\bin` contains x86\_64-w64-mingw32-gcc.exe
-   open a cmd.exe and do `set PATH=C:\mingw64\bin;%PATH%` for 64-bit
    building. `set PATH=C:\mingw32\bin;%PATH%` for 32-bit building.
-   You should be ready to go. Execute `i686-w64-mingw32-gcc -v` or
    `x86_86-w64-mingw32-gcc -v` to see that everything has gone well.
-   (Autobuilds only) If you need mingw32-make, please download it from
    the mingw-w64 downloads site under External binary packages.

### Linux

Several distributions already provide mingw64 packages:

-   Arch (AUR):
    <a href="https://aur.archlinux.org/packages.php?ID=53926"
    rel="nofollow">https://aur.archlinux.org/packages.php?ID=53926</a>
-   Debian: <a href="http://packages.debian.org/sid/mingw-w64"
    rel="nofollow">http://packages.debian.org/sid/mingw-w64</a> and
    related packages.
-   Fedora: <a href="https://fedoraproject.org/wiki/MinGW/Tutorial"
    rel="nofollow">https://fedoraproject.org/wiki/MinGW/Tutorial</a>
-   Ubuntu: <a href="http://packages.ubuntu.com/source/lucid/mingw-w64"
    rel="nofollow">http://packages.ubuntu.com/source/lucid/mingw-w64</a>
    and related packages

## Using the Toolchain

The toolchain consists of compilers, linkers assemblers and supporting
utilities (comparable to what you get with the Windows SDK. It does not
include an IDE.

If you need to compile GNU software which requires the use of a
configure script for Windows, see [MSYS](./msys.md).

CMake can be used for generating "MinGW Makefiles", which of course work
fine for mingw-w64/w32.