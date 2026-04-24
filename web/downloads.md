# Pre-built Toolchains

While mingw-w64 provides the core Windows headers and libraries needed for
Windows development, it's not very useful on its own. Most users should install
a pre-built toolchain that combines mingw-w64 with a compiler (like GCC with
binutils, or LLVM/Clang) and other essential build components. These
distributions package everything needed to compile programs for Windows and are
much easier to set up than building from source.

## Pre-built toolchains and packages

<table>
    <tbody>
        <tr>
            <th>
            </th>
            <th>Version </th>
            <th>Host </th>
            <th>GCC / mingw-w64 Version </th>
            <th>Languages </th>
            <th>Additional Software in Package Manager </th>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#arch-linux"><img
                            src="../logos/archlinux-logo.png"
                            title="Arch Linux logo" alt="Arch Linux logo" width="32"></a><br><a
                        href="#arch-linux"> Arch
                        Linux</a></strong>
            </td>
            <td>Rolling</td>
            <td>Linux</td>
            <td>
                <a href="https://archlinux.org/packages/extra/x86_64/mingw-w64-gcc/" class="urlextern"
                    title="https://archlinux.org/packages/extra/x86_64/mingw-w64-gcc/" rel="nofollow">15.2.0</a>/<a
                    href="https://archlinux.org/packages/extra/any/mingw-w64-crt/" class="urlextern"
                    title="https://archlinux.org/packages/extra/any/mingw-w64-crt/" rel="nofollow">13.0.0</a>
            </td>
            <td>Ada, C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td><a href="https://aur.archlinux.org/packages/?K=mingw-w64">many</a></td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#cygwin"><img
                            src="../logos/cygwin-logo.png"
                            title="Cygwin logo" alt="Cygwin logo" width="32"></a><br>
                            <a href="#cygwin">Cygwin</a></strong>
            </td>
            <td>Rolling</td>
            <td>Windows</td>
            <td>
                <a href="https://cygwin.com/packages/summary/mingw64-x86_64-gcc-src.html" class="urlextern"
                    title="https://cygwin.com/packages/summary/mingw64-x86_64-gcc-src.html" rel="nofollow">13.4.0</a>/<a
                    href="https://cygwin.com/packages/summary/mingw64-x86_64-runtime-src.html" class="urlextern"
                    title="https://cygwin.com/packages/summary/mingw64-x86_64-runtime-src.html" rel="nofollow">13.0.0</a>
            </td>
            <td>C, C++, Fortran, Obj-C </td>
            <td><a href="https://cygwin.com/cgi-bin2/package-grep.cgi?grep=mingw64-x86_64&arch=x86_64"> many</a> </td>
        </tr>
        <tr>
            <td style="text-align:center;" rowspan="3">
                <strong><a href="#debian"><img src="../logos/debian-logo.png" title="Debian logo" alt="Debian logo" width="32"></a>
                <br>
                <a href="#debian">Debian</a></strong>
            </td>
            <td colspan="2">Debian 11 (Bullseye) </td>
            <td>10.2.1/8.0.0 </td>
            <td rowspan="3">Ada, C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td rowspan="3">9 (gdb, libassuan, libgcrypt, libgpg-error, libksba, libnpth, nsis, win-iconv, zlib) </td>
        </tr>
        <tr>
            <td colspan="2">Debian 12 (Bookworm) </td>
            <td>12.0.0/10.0.0 </td>
        </tr>
        <tr>
            <td colspan="2">Debian 13 (Trixie) </td>
            <td>14.2.0/12.0.0 </td>
        </tr>
        <tr>
            <td style="text-align:center;" rowspan="2">
                <strong><a href="#fedora"><img
                            src="../logos/fedora-logo.png"
                            title="Fedora Linux logo" alt="Fedora Linux logo" width="32"></a><br><a
                        href="#fedora">Fedora</a></strong>
            </td>
            <td colspan="2">Fedora 42</td>
            <td>14.2.1/12.0.0</td>
            <td rowspan="2">Ada, C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td rowspan="2"><a href="https://packages.fedoraproject.org/search?query=mingw64"> many</td>
        </tr>
        <tr>
            <td colspan="2">Fedora 43</td>
            <td>15.2.1/13.0.0</td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#gcc-mcf">GCC-MCF</a></strong>
            </td>
            <td>Rolling</td>
            <td>Windows</td>
            <td>16.x.x/trunk</td>
            <td>C, C++, Fortran, Obj-C, Obj-C++</td>
            <td>20 (boost, bzip2, cmake, curl, gdb, iconv, lua, make, meson, muon, ncurses, ninja,
                openssl, python, sqlite3, upx, xmake, yasm, zlib, zstd) </td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#homebrew">Homebrew</a></strong>
            </td>
            <td>Rolling </td>
            <td>macOS</td>
            <td>
                <a href="https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/m/mingw-w64.rb"
                    class="urlextern"
                    title="https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/m/mingw-w64.rb"
                    rel="nofollow">15.2.0</a>/<a
                    href="https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/m/mingw-w64.rb"
                    class="urlextern"
                    title="https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/m/mingw-w64.rb"
                    rel="nofollow">13.0.0</a>
            </td>
            <td>C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td>1 (nsis)</td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#llvm-mingw">LLVM-MinGW</a></strong>
            </td>
            <td>20251202</td>
            <td>Windows, Linux, macOS</td>
            <td>LLVM 21.1.7/trunk</td>
            <td>C, C++</td>
            <td>make, Python</td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#macports"><img
                            src="../logos/macports-logo.png"
                            title="MacPorts logo" alt="MacPorts logo" width="32"></a><br><a
                        href="#macports">
                        MacPorts</a></strong>
            </td>
            <td>Rolling </td>
            <td>macOS</td>
            <td>
                <a href="https://github.com/macports/macports-ports/blob/master/cross/x86_64-w64-mingw32-gcc/Portfile"
                    class="urlextern"
                    title="https://github.com/macports/macports-ports/blob/master/cross/x86_64-w64-mingw32-gcc/Portfile"
                    rel="nofollow">15.2.0</a>/<a
                    href="https://github.com/macports/macports-ports/blob/master/cross/mingw-w64/Portfile"
                    class="urlextern"
                    title="https://github.com/macports/macports-ports/blob/master/cross/mingw-w64/Portfile"
                    rel="nofollow">13.0.0</a>
            </td>
            <td>C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td>1 (nsis)</td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#mingw-w64-builds">MinGW-W64-builds</a></strong>
            </td>
            <td>Rolling </td>
            <td>Windows</td>
            <td>15.2.0/13.0.0 </td>
            <td>C, C++, Fortran </td>
            <td>4 (gdb, libiconf, python, zlib) </td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#msys2" class="media" title="download:msys2"><img
                            src="../logos/msys2-logo.png"
                            title="MSYS2 logo" alt="MSYS2 logo" width="32"></a><br>
                            <a href="#msys2">MSYS2</a></strong>
            </td>
            <td>Rolling </td>
            <td>Windows</td>
            <td>
                <a href="https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-gcc/PKGBUILD" class="urlextern"
                    title="https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-gcc/PKGBUILD"
                    rel="nofollow">15.2.0</a>/<a
                    href="https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-crt/PKGBUILD"
                    class="urlextern"
                    title="https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-crt/PKGBUILD"
                    rel="nofollow">trunk</a>
            </td>
            <td>Ada, C, C++, Fortran, Obj-C, Obj-C++, OCaml </td>
            <td><a href="https://packages.msys2.org">many</a></td>
        </tr>
        <tr>
            <td style="text-align:center;" rowspan="3">
                <strong><a href="#ubuntu"><img
                            src="../logos/ubuntu-logo.png"
                            title="Ubuntu logo" alt="Ubuntu logo" width="32"></a><br><a href="#ubuntu"> Ubuntu</a></strong>
            </td>
            <td colspan="2">22.04 Jammy Jellyfish </td>
            <td>10.3.0/8.0.0 </td>
            <td rowspan="3">Ada, C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td rowspan="3">9 (gdb, libassuan, libgcrypt, libgpg-error, libksba, libnpth, nsis, win-iconv, zlib) </td>
        </tr>
        <tr>
            <td colspan="2">24.04 Noble Numbat </td>
            <td>13.2.0/11.0.1 </td>
        </tr>
        <tr>
            <td colspan="2">25.10 Questing Quokka </td>
            <td>13.2.0/12.0.0 </td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#w64devkit">w64devkit</a></strong>
            </td>
            <td>2.7.0</td>
            <td>Windows</td>
            <td>15.2.0/14.0.0</td>
            <td>C, C++, Fortran</td>
            <td>
                10
                (busybox,
                ccache,
                cmake,
                ctags,
                gdb,
                make,
                ninja,
                pkg-config,
                vim,
                zstd)
            </td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#winlibscom">WinLibs.com</a></strong>
            </td>
            <td>Rolling </td>
            <td>Windows</td>
            <td>
                <a href="https://winlibs.com/#download-release" class="urlextern"
                    title="https://winlibs.com/"
                    rel="nofollow">15.2.0/13.0.0</a>
            </td>
            <td>Ada, C, C++, Fortran, Obj-C, Obj-C++, Assembler</td>
            <td>Package manager: work in progress (will offer > 2500 packages)</td>
        </tr>
    </tbody>
</table>

#### Arch Linux

On Arch Linux, mingw-w64 headers and runtime libraries for cross-compilation can
be installed with the integrated package manager, `pacman`. Usually they are
installed as dependencies of `mingw-w64-gcc`. See [Getting Started](./getting-started/archlinux.md).

* [Extra repository (toolchain)](https://www.archlinux.org/packages/?q=mingw-w64)
* [AUR repository (additional packages)](https://aur.archlinux.org/packages/?SeB=n&K=mingw-w64&SB=c&PP=250)

#### Cygwin

[Cygwin](https://cygwin.com) is a Unix-like environment and command-line
interface for Microsoft Windows. Its core is the cygwin1.dll library which
provides POSIX functionality on top of the Win32 API. It can be used as a build
environment which targets Windows directly and for which output doesn't depend
on cygwin1.dll.

As part of the numerous packages in cygwin, there are cross-compilation
toolchains which target both 32 bits and 64 bits; their names start with
“mingw64-”, and can be installed with Cygwin's package manager,
[setup-x86_64.exe](https://cygwin.com/install.html).

Once they are installed, they should be used according to the general
cross-compilation approach.

#### Debian

On Debian and systems that derive from Debian, mingw-w64 headers and runtime
libraries for cross-compilation can be installed with the integrated package
manager, `apt` or `aptitude`. Usually they are installed as dependencies of
`g++-mingw-w64`. See [Getting Started](./getting-started/debian.md).

Debian provides separate packages for `gcc` and `g++`, and separate packages
for `posix` and `win32` thread models, and (since Debian Trixie) also separate
packages for UCRT.

Here is the list of [mingw-w64 packages on Debian](https://packages.debian.org/mingw-w64).

#### Fedora

On Fedora, mingw-w64 headers and runtime libraries for cross-compilation can be
installed with the integrated package manager, `dnf`. Usually they are installed
as dependencies of `mingw64-gcc-c++`. See [Getting Started](./getting-started/fedora.md).

Fedora provides separate packages for UCRT on x86-64.

#### GCC-MCF

[GCC with the MCF thread model](https://gcc-mcf.lhmouse.com/) is a series of
x86-32 and x86-64 native toolchains built by LH_Mouse. The MCF thread model has
been merged into GCC 13, and can be enabled by passing `--enable-threads=mcf` to
GCC's _configure_ script. C++11 threading facilities, such as `std::thread`,
`std::mutex`, `std::condition_variable`, `std::call_once`, `thread_local` etc.
invoke the [mcfgthread](https://github.com/lhmouse/mcfgthread/) library, which
implements them on Windows syscalls in a more standard-compliant and more
efficient way, outperforming even native slim reader/write locks (SRW) since
Windows 7.

GCC-MCF provides standalone [7-Zip archives](https://gcc-mcf.lhmouse.com/) of
complete toolchains, including mingw-w64 headers, libraries, compilers and
linkers.

#### Homebrew

With Homebrew, mingw-w64 headers, libraries, compilers and linkers can be
installed with just `brew install mingw-w64`.

#### LLVM-MinGW

LLVM-MinGW is a toolchain built with Clang, LLD, libc++, targeting
i686, x86-64, ARM and AArch64 (ARM64), with releases both for running
as a cross compiler from Linux and for running on Windows. It supports
AddressSanitizer, UndefinedBehaviorSanitizer, and generating debug
info in PDB format.

LLVM-MinGW provides [standalone tarballs](https://github.com/mstorsjo/llvm-mingw/releases)
of complete toolchains, including mingw-w64 headers, libraries, compilers and
linkers.

#### MacPorts

To install just the 32-bit or just 64-bit compiler with dependencies, use:

```
sudo port install i686-w64-mingw32-gcc
sudo port install x86_64-w64-mingw32-gcc
```

A shortcut to install both:

```
sudo port install mingw-w64
```

Here is the list of [mingw-w64 packages on MacPorts](https://www.macports.org/ports.php?by=name&substr=mingw).

#### MinGW-W64-builds

Installation: [GitHub](https://github.com/niXman/mingw-builds-binaries/releases)

#### MSYS2

[MSYS2](https://www.msys2.org/) is a series of Unix-like environments on
Windows. It has a package manager, and provides separate environments (shells):

* `MSYS` is for programs that are linked against the MSYS2 (Cygwin) runtime, and not mingw-w64.
* `MINGW32` is for programs that are compiled by GCC and linked against mingw-w64 and MSVCRT.DLL on x86.
* `MINGW64` is for programs that are compiled by GCC and linked against mingw-w64 and MSVCRT.DLL on x64.
* `UCRT64` is for programs that are compiled by GCC and linked against mingw-w64 and UCRT on x64.
* `CLANG64` is for programs that are compiled by Clang and linked against mingw-w64 and UCRT on x64.
* `CLANGARM64` is for programs that are compiled by Clang and linked against mingw-w64 and UCRT on ARM64.

Mingw-w64 headers, libraries, compilers and linkers can be installed with the
MSYS2 package manager, `pacman`. Each environment has its own naming schemes of
packages. See [Getting Started for UCRT64](./getting-started/msys2.md)
or [Getting Started for CLANG64](./getting-started/msys2-llvm.md).

Here is the list of [mingw-w64 packages in UCRT64](https://packages.msys2.org/packages/?repo=ucrt64)
and [mingw-w64 packages in CLANG64](https://packages.msys2.org/packages/?repo=clang64).

#### Ubuntu

On Ubuntu and Linux Mint, mingw-w64 headers and runtime libraries for
cross-compilation can be installed with the integrated package
manager, `apt` or `aptitude`. Usually they are installed as dependencies of
`g++-mingw-w64`. See [Getting Started](./getting-started/debian.md).

Ubuntu provides separate packages for `gcc` and `g++`, and separate packages
for `posix` and `win32` thread models.

Here is the list of [mingw-w64 packages on Ubuntu](https://launchpad.net/ubuntu/+source/mingw-w64).

#### w64devkit

[w64devkit][w64devkit] is a portable C and C++ development kit for x64 (and x86) Windows.

Included tools:

* mingw-w64 GCC : compilers, linker, assembler
* [GDB][gdb] : debugger
* [GNU Make][make] : standard build tool
* [CMake][cmake] with [Ninja][ninja]: build system
* [busybox-w32][bb] : standard unix utilities, including sh
* [Vim][vim] : powerful text editor
* [Universal Ctags][ctags] : source navigation
* [Ccache][ccache] : compiler cache

The toolchain includes pthreads, C++11 threads, and OpenMP. All included
runtime components are static.

Installation: [GitHub](https://github.com/skeeto/w64devkit/releases)

[bb]: https://frippery.org/busybox/
[ccache]: https://ccache.dev/
[cmake]: https://cmake.org/
[ctags]: https://github.com/universal-ctags/ctags
[gdb]: https://www.gnu.org/software/gdb/
[make]: https://www.gnu.org/software/make/
[ninja]: https://ninja-build.org/
[vim]: https://www.vim.org/
[w64devkit]: https://github.com/skeeto/w64devkit

#### WinLibs.com

Standalone mingw-w64+GCC builds for Windows, built from scratch (including all dependencies) natively on Windows for Windows.

Downloads are archive files (`.zip` or `.7z`). No installation is required,
just extract the archive and start using the programs in `mingw32\bin` or  `mingw64\bin`.
This allows for a relocatable compiler suite and allows having multiple versions on the same system.

Also contains other tools including:

* GDB - the GNU Project debugger
* GNU Binutils - a collection of binary tools
* GNU Make - a tool which controls the generation of executables and other non-source files
* Yasm - The Yasm Modular Assembler Project
* NASM - The Netwide Assembler
* JWasm - A free MASM-compatible assembler

Flavors:

* separate packages for 32-bit (i686) and 64-bit (x86_64) Windows
* separate packages for MSVCRT and UCRT builds
* only POSIX threads builds (which also include Win32 API thread functions)
* exception model: Dwarf for 32-bit (i686) and SEH for 64-bit (x86_64)

Installation: Download from [winlibs.com](https://winlibs.com/) and extract archive (no installation needed).

## Unsorted complementary list

### OpenSUSE

The [OpenSUSE Linux distribution](https://www.opensuse.org) also has a large and
well-maintained set of packages for cross-compilation.
