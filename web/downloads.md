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
                    title="https://archlinux.org/packages/extra/x86_64/mingw-w64-gcc/" rel="nofollow">14.2.0</a>/<a
                    href="https://archlinux.org/packages/extra/any/mingw-w64-crt/" class="urlextern"
                    title="https://archlinux.org/packages/extra/any/mingw-w64-crt/" rel="nofollow">12.0.0</a>
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
                    title="https://cygwin.com/packages/summary/mingw64-x86_64-gcc-src.html" rel="nofollow">12.4.0</a>/<a
                    href="https://cygwin.com/packages/summary/mingw64-x86_64-runtime-src.html" class="urlextern"
                    title="https://cygwin.com/packages/summary/mingw64-x86_64-runtime-src.html" rel="nofollow">12.0.0</a>
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
            <td colspan="2">Debian 10 (Buster) </td>
            <td>8.3.0/6.0.0 </td>
            <td rowspan="3">Ada, C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td rowspan="3">9 (gdb, libassuan, libgcrypt, libgpg-error, libksba, libnpth, nsis, win-iconv, zlib) </td>
        </tr>
        <tr>
            <td colspan="2">Debian 11 (Bullseye) </td>
            <td>10.2.1/8.0.0 </td>
        </tr>
        <tr>
            <td colspan="2">Debian 12 (Bookworm) </td>
            <td>12.0.0/10.0.0 </td>
        </tr>
        <tr>
            <td style="text-align:center;" rowspan="2">
                <strong><a href="#fedora"><img
                            src="../logos/fedora-logo.png"
                            title="Fedora Linux logo" alt="Fedora Linux logo" width="32"></a><br><a
                        href="#fedora" > Fedora</a></strong>
            </td>
            <td colspan="2">Fedora 40 </td>
            <td>14.1.1/11.0.1 </td>
            <td rowspan="2">Ada, C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td rowspan="2"><a href="https://packages.fedoraproject.org/search?query=mingw64"> many</td>
        </tr>
        <tr>
            <td colspan="2">Fedora 41 </td>
            <td>14.2.1/12.0.0 </td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#llvm-mingw">LLVM-MinGW</a></strong>
            </td>
            <td>20240518</td>
            <td>Windows, Linux, macOS</td>
            <td>LLVM 18.1.6/trunk</td>
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
                    rel="nofollow">14.2.0</a>/<a
                    href="https://github.com/macports/macports-ports/blob/master/cross/mingw-w64/Portfile"
                    class="urlextern"
                    title="https://github.com/macports/macports-ports/blob/master/cross/mingw-w64/Portfile"
                    rel="nofollow">12.0.0</a>
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
            <td>13.1.0/11.0.0 </td>
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
                    rel="nofollow">14.2.0</a>/<a
                    href="https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-crt-git/PKGBUILD"
                    class="urlextern"
                    title="https://github.com/msys2/MINGW-packages/blob/master/mingw-w64-crt-git/PKGBUILD"
                    rel="nofollow">trunk</a>
            </td>
            <td>Ada, C, C++, Fortran, Obj-C, Obj-C++, OCaml </td>
            <td><a href="https://packages.msys2.org">many</a></td>
        </tr>
        <tr>
            <td style="text-align:center;" rowspan="4">
                <strong><a href="#ubuntu"><img
                            src="../logos/ubuntu-logo.png"
                            title="Ubuntu logo" alt="Ubuntu logo" width="32"></a><br><a href="#ubuntu"> Ubuntu</a></strong>
            </td>
            <td colspan="2"> 20.04 Focal Fossa </td>
            <td>9.3.0/7.0.0 </td>
            <td rowspan="4">Ada, C, C++, Fortran, Obj-C, Obj-C++ </td>
            <td rowspan="4">9 (gdb, libassuan, libgcrypt, libgpg-error, libksba, libnpth, nsis, win-iconv, zlib) </td>
        </tr>
        <tr>
            <td colspan="2"> 22.04 Jammy Jellyfish </td>
            <td>10.3.0/8.0.0 </td>
        </tr>
        <tr>
            <td colspan="2"> 24.04 Noble Numbat </td>
            <td>13.2.0/11.0.1 </td>
        </tr>
        <tr>
            <td colspan="2"> 24.10 Oracular Oriole </td>
            <td>14.1.0/12.0.0 </td>
        </tr>
        <tr>
            <td style="text-align:center;">
                <strong><a href="#w64devkit">w64devkit</a></strong>
            </td>
            <td>2.0.0</td>
            <td>Windows</td>
            <td>14.2.0/12.0.0</td>
            <td>C, C++, Fortran</td>
            <td>
                8
                (busybox,
                cppcheck,
                ctags,
                gdb,
                make,
                nasm,
                pkg-config,
                vim)
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
                    rel="nofollow">13.2.0</a>
            </td>
            <td>Ada, C, C++, Fortran, Obj-C, Obj-C++, Assembler</td>
            <td>Package manager: work in progress (will offer > 2500 packages)</td>
        </tr>
    </tbody>
</table>

#### Arch Linux

Installation:

* [Extra repository (toolchain)](https://www.archlinux.org/packages/?q=mingw-w64)
* [AUR repository (additional packages)](https://aur.archlinux.org/packages/?SeB=n&K=mingw-w64&SB=c&PP=250)

#### Cygwin

[Cygwin](https://cygwin.com) is a Unix-like environment and command-line
interface for Microsoft Windows. Its core is the cygwin1.dll library which
provides POSIX functionality on top of the Win32 API. It can be used as a build
environment which targets Windows directly and for which output doesn't depend
on cygwin1.dll.

Installation is done through cygwin's package manager:
[setup.exe](https://cygwin.com/install.html).

As part of the numerous packages in cygwin, there are cross-compilation
toolchains which target both 32 bits and 64 bits; their names start with
“mingw64-”.

Once they are installed, they should be used according to the general
cross-compilation approach.

#### Debian

Installation: through integrated package manager.

[mingw-w64 packages on Debian](https://packages.debian.org/mingw-w64)

#### Fedora

Installation: through integrated package manager.

#### LLVM-MinGW

LLVM-MinGW is a toolchain built with Clang, LLD, libc++, targeting
i686, x86\_64, arm and aarch64 (ARM64), with releases both for running
as a cross compiler from Linux and for running on Windows. It supports
Address Sanitizer, Undefined Behaviour Sanitizer, and generating debug
info in PDB format.

Installation: [GitHub](https://github.com/mstorsjo/llvm-mingw/releases)

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

Installation: [GitHub](https://www.msys2.org/)

#### Ubuntu

Installation: through integrated package manager.

[mingw-w64 packages on Ubuntu](https://launchpad.net/ubuntu/+source/mingw-w64)

#### w64devkit

[w64devkit][w64devkit] is a portable C and C++ development kit for x64 (and x86) Windows.

Included tools:

* mingw-w64 GCC : compilers, linker, assembler
* [GDB][gdb] : debugger
* [GNU Make][make] : standard build tool
* [busybox-w32][bb] : standard unix utilities, including sh
* [Vim][vim] : powerful text editor
* [Universal Ctags][ctags] : source navigation
* [NASM][nasm] : x86 assembler
* [Cppcheck][cppcheck] : static code analysis

The toolchain includes pthreads, C++11 threads, and OpenMP. All included
runtime components are static.

Installation: [GitHub](https://github.com/skeeto/w64devkit/releases)

[bb]: https://frippery.org/busybox/
[cppcheck]: https://cppcheck.sourceforge.io/
[ctags]: https://github.com/universal-ctags/ctags
[gdb]: https://www.gnu.org/software/gdb/
[make]: https://www.gnu.org/software/make/
[nasm]: https://www.nasm.us/
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

### GCC with the MCF thread model

[GCC with the MCF thread model](https://gcc-mcf.lhmouse.com/) is a series of
x86 and x64 native toolchains built by LH_Mouse. The MCF thread model has been
merged into GCC 13, and can be enabled by passing `--enable-threads=mcf` to
GCC's _configure_ script. C++11 threading facilities, such as `std::thread`,
`std::mutex`, `std::condition_variable`, `std::call_once`, `thread_local` etc.
invoke the [mcfgthread](https://github.com/lhmouse/mcfgthread/) library, which
implements them on Windows syscalls in a more standard-compliant and more
efficient way, outperforming even native slim reader/write locks (SRW) since
Windows Vista.

### OpenSUSE

The [OpenSUSE Linux distribution](https://www.opensuse.org) also has a large and
well-maintained set of packages for cross-compilation.
