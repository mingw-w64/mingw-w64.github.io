# Overview

Mingw-w64 is an advancement of the original mingw.org project, created to
support the GCC compiler on Windows systems. It has forked it in 2007 in order
to provide support for 64 bits and new APIs. It has since then gained widespread
use and distribution.

The development and community are very active and welcoming with new
contributors every month and simple installers.

## Headers, Libraries and Runtime

- More than a million lines of headers are provided, not counting generated ones,
  and regularly expanded to track new Windows APIs.
- Everything needed for linking and running your code on Windows.
- Winpthreads, a pthreads library for C++11 threading support and simple
  integration with existing project.
- Winstorecompat, a work-in-progress convenience library that eases conformance with the Windows Store.
- Better-conforming and faster math support compared to VisualStudio's.

## Tools

- gendef: generate Visual Studio .def files from .dll files.
- genidl: generate .idl files from .dll files.
- widl: compile .idl files.

## Friend projects

Mingw-w64 interacts a lot with other projects in order to help everyone move
forward. Contributions have been going to and coming from these projects:

<table>
<tr>
<td style="text-align: center">
    <a href="http://cygwin.com" class="media" title="http://cygwin.com"><img src="./logos/cygwin-logo.png" title="Cygwin" width="64" height="64" alt="Cygwin" />
    <br>Cygwin
    </a>
</td>
<td style="text-align: center">
    <a href="http://reactos.com" class="media" title="http://reactos.com"><img src="./logos/reactos-logo.png" title="ReactOS" width="116" height="64" alt="ReactOS" />
    <br>
    ReactOS
    </a>
</td>
<td style="text-align: center">
    <a href="http://winehq.org" class="media" title="http://winehq.org"><img src="./logos/wine-logo.png" title="Wine" width="40" height="64" alt="Wine" />
    <br>
    Wine
    </a>
</td>
</tr>
</table>

## Some Projects using Mingw-w64

- [Fedora cross-compiler](http://fedoraproject.org/wiki/MinGW)
- [Npackd](https://npackd.appspot.com)
- [OpenSUSE](http://opensuse.org)
- [Win-builds](http://win-builds.org)
- [Barchart-UDT](http://code.google.com/p/barchart-udt/)
- [Blender](http://www.blender.org/)
- [Boost](http://www.boost.org/)
- [Botan](http://botan.randombit.net/)
- [Ceemple](http://www.ceemple.com)
- [Code::Blocks](http://www.codeblocks.org/)
- [DAE Tools](http://daetools.sourceforge.net)
- [devkitPro](http://devkitpro.org/)
- [Disk Based HashTables](http://sourceforge.net/projects/dbh/)
- [Ecere SDK](http://www.ecere.org/)
- [Ekiga](http://www.ekiga.org/)
- [Emerge Desktop](http://emergedesktop.org)
- [Enlightenment](http://www.enlightenment.org/)
- [Factor](http://factorcode.org/)
- [FFmpeg](http://ffmpeg.mplayerhq.hu/)
- [FLTK](http://www.fltk.org/)
- [Freecell Solver](http://fc-solve.shlomifish.org/)
- [Freeverb3](http://freeverb3.sourceforge.net/)
- [GCC: The GNU Compiler Collection](http://gcc.gnu.org/)
- [GDB: The GNU Project Debugger](http://www.gnu.org/software/gdb/)
- [GIMP](http://gimp-win.sourceforge.net/stable.html)
- [GNU Binutils](http://www.gnu.org/software/binutils/)
- [GNU SASL](http://www.gnu.org/software/gsasl/)
- [GnuTLS](http://www.gnu.org/software/gnutls/)
- [GraphicsMagick](http://www.graphicsmagick.org/)
- [GTK+](http://www.gtk.org/download-windows-64bit.html)
- [Hexen II: Hammer of Thyrion](http://uhexen2.sf.net/)
- [iAuxSoft](http://www.iauxsoft.com/)
- [ImageMagick](http://www.imagemagick.org/)
- [JPen](http://jpen.sf.net/)
- [KDE Software Collection](http://kde.org/)
- [libav](http://libav.org/)
- [LibreOffice](http://www.libreoffice.org/)
- [libsndfile](http://www.mega-nerd.com/libsndfile/)
- [libvirt](http://libvirt.org/)
- [libvpx](http://www.webmproject.org/)
- [Libxml2](http://xmlsoft.org/)
- [MAME (Yes, the arcade emulator!)](http://mamedev.org/)
- [ManKai Common Lisp](http://common-lisp.net/project/mkcl/)
- [mCtrl](http://mctrl.org)
- [mpg123](http://www.mpg123.de/)
- [MPIR](http://www.mpir.org/)
- [MS MPI (repackaged)](https://bitbucket.org/Haroogan/microsoft-mpi/downloads)
- [MS MPI](http://www.symscape.com/configure-msmpi-for-mingw-w64)
- [OCaml](http://www.ocaml.org)
- [OpenFOAM](http://www.symscape.com/openfoam-1-7-x-on-windows-64-mpi)
- [OpenLisp](http://www.eligis.com/)
- [OpenSC](http://www.opensc-project.org/)
- [OpenSSL](http://www.openssl.org/)
- [OpenTURNS](http://www.openturns.org/)
- [Perl (5.12.0 and later)](http://www.perl.org/)
- [PostgreSQL](http://www.postgresql.org/)
- [pthreads](http://sourceware.org/pthreads-win32/)
- [PToolsWin](http://www.paratools.com/PToolsWIN)
- [QEMU](http://qemu.org)
- [Qt](http://qt-project.org/)
- [QuakeSpasm](http://quakespasm.sourceforge.net/)
- [ReMooD](http://remood.sf.net/)
- [SBC Archiver](http://sbcarchiver.cjb.net/)
- [Smart Image Denoiser](http://smartimagedenoiser.com/)
- [smartmontools](http://smartmontools.sourceforge.net/)
- [Strawberry Perl (bundles C toolchains)](http://strawberryperl.com/)
- [strongSwan](http://strongswan.org/)
- [The R Project for Statistical Computing](http://www.r-project.org/)
- [Tomahawk Player](http://www.tomahawk-player.org/)
- [VideoLAN VLC](http://www.videolan.org/vlc/)
- [VSXu](http://www.vsxu.com/)
- [Woo](http://www.woodem.eu/)
- [wxPerl PPMs](http://www.wxperl.co.uk/building/msw.html)
- [wxWidgets](http://www.wxwidgets.org/)
- [YafaRay](http://www.yafaray.org/)
- [zlib](http://www.zlib.net/)