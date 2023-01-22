# Cross Win32 and Win64 compiler

How to build a Mingw-w64 x86\_64-w64-mingw32 cross-compiler.

## About this document

(At this time, building a native compiler is suggested. Documentation to
follow. This is all still required to be able to build it.) Top-level
configure to do this all with one command is also to follow.

As of 2009-05-31, x86\_64-pc-mingw32 has been replaced by
x86\_64-w64-mingw32. The change allows for mingw-w64 to have a
host/target type independent of mingw.org's MinGW.

All default libraries work! We are now in a functional beta stage.

This file describes how to build the Mingw-w64 GCC toolchain as a
cross-compiler on Cygwin, MinGW with MSys, and \*nix shells.

Cygwin 1.7 currently supported. This document recommends and assumes
Bash (for Cygwin, Unix), or MSys core sh default shells are used.

## Targeted audience

This document is written to help those new to building the mingw-w64
cross compilers on Windows using MSYS/MinGW and Cygwin. It can also be
adapted slightly for building the mingw-w64 cross compiler on Linux.

For a more advanced guide on building the mingw-w64 cross compiler
including the optional dependencies, please refer to the
"mingw-w64-howto-build-adv.txt" guide.

## Version changes

Date  
Version  
Author

2007-07-31  
1.0  
Kai Tietz &lt;Kai.Tietz at onevision.com&gt;

2007-08-20  
1.1  
Kai Tietz &lt;Kai.Tietz at onevision.com&gt;

2007-08-21  
1.2  
NightStrike? &lt;nightstrike at gmail.com&gt;

2007-10-01  
1.3  
NightStrike? &lt;nightstrike at gmail.com&gt;

2007-11-27  
1.4  
NightStrike? &lt;nightstrike at gmail.com&gt;

2009-05-31  
1.5  
Xenofears &lt;xenofears at gmail.com&gt;

2009-06-06  
1.6  
Xenofears &lt;xenofears at gmail.com&gt;

2009-08-28  
1.7  
Xenofears &lt;xenofears at gmail.com&gt;

2009-08-30  
1.8  
Ozkan Sezer &lt;sezeroz at gmail dot com&gt;

2009-10-09  
1.9  
Jonathan Yong
&lt;jon\_y<a href="../a" class="alink notfound">[a]</a>users.sourceforge.com&gt;

2010-02-28  
1.10  
Ozkan Sezer &lt;sezeroz at gmail dot com&gt;

2010-08-31  
1.11  
Jonathan Yong
&lt;jon\_y<a href="../a" class="alink notfound">[a]</a>users.sourceforge.com&gt;

2010-10-05  
1.12  
Nicolas Guillaumin

2013-01-21  
1.13  
Jonathan Yong
&lt;jon\_y<a href="../a" class="alink notfound">[a]</a>users.sourceforge.com&gt;

## Table of Contents

-   Requirements <a href="../RQRMTS" class="alink notfound">[RQRMTS]</a>
-   Optional <a href="../OPTNLB" class="alink notfound">[OPTNLB]</a>
-   Download new packages
    <a href="../DWNWPK" class="alink notfound">[DWNWPK]</a>
-   Build type options
    <a href="../BTYOPT" class="alink notfound">[BTYOPT]</a>
-   Building binutils cross toolchain
    <a href="../CRSBNT" class="alink notfound">[CRSBNT]</a>
-   Install the Mingw-w64 header set and create required symlinks
    <a href="../HDRSYM" class="alink notfound">[HDRSYM]</a>
-   Building the GCC core cross-compiler
    <a href="../BDGCOR" class="alink notfound">[BDGCOR]</a>
-   Building the crt
    <a href="../BLDCRT" class="alink notfound">[BLDCRT]</a>
-   Finishing GCC
    <a href="../FNSHGC" class="alink notfound">[FNSHGC]</a>
-   Path update and using your new cross-compiler
    <a href="../PTHUPD" class="alink notfound">[PTHUPD]</a>

You can search the keys (i.e.
<a href="../BLDCRT" class="alink notfound">[BLDCRT]</a>) to jump to that
section.

## Requirements

<a href="../RQRMTS" class="alink notfound">[RQRMTS]</a>

You will need a complete GCC toolchain for the host system (Cygwin,
MinGW/MSys or Linux), which usually includes all of the required
components:

-   GCC (for the native platform)
-   Binutils (for the native platform)
-   Bison
-   Flex
-   gperf (Optional, for developing on GCC)
-   Coreutils
-   Make (3.81 or newer)
-   GMP 4.3.1 or newer
    <a href="../found%20on%20Cygwin%20setup%20under%20math"
    class="alink notfound">[found on Cygwin setup under math]</a>
-   MPFR 2.4.1 or newer
    <a href="../found%20on%20Cygwin%20setup%20under%20math"
    class="alink notfound">[found on Cygwin setup under math]</a>
-   Perl (optional for pod2man)

## Optional

<a href="../OPTNLB" class="alink notfound">[OPTNLB]</a>

Optional for source download / version management:

-   CVS
-   Subversion (SVN)
-   wget
-   tar & gzip/bzip2

Optional for optimization enhancements: (Math toolchain dependencies are
elaborated on GMP)

-   PPL 0.10 or newer
-   ClooG-PPL 0.15 or newer (must be ppl)
-   MPC 0.7 or newer

To build with MSys (Minimal SYStem for Win32), to satisfy the
requirements download and install functional MinGW (GCC toolchain), MSYS
(sh shell), bison, and flex.

If your host OS is Vista, you must install SP1 or SP2! If you can't, you
must use an unoptimized collect2.exe as a workaround, but you are on
your own.

Win32 installers to use with mingw msys available for download at
MinGW's sourceforge page:
<http://sourceforge.net/project/showfiles.php?group_id=23617>

GMP & MPFR sources may be placed in the GCC source tree root in
directories with their names and they will be built automatically by
GCC's configure (as static libs). You might need to make install from
inside the directories if GCC doesn't do it for you.

## Download new packages

<a href="../DWNWPK" class="alink notfound">[DWNWPK]</a>

You need to download the following packages:

-   At least CVS snapshot (2.20.51). Note that 2.20.1 is not supported
    due to ABI changes.
-   GCC version 4.5.1 release for stable, or latest GCC (4.6) snapshot
    or svn co for experimental. GCC-4.3 support is no longer maintained.
-   Current Mingw-w64 release available at
    <http://sourceforge.net/projects/mingw-w64> . Snapshot, even better
    from SVN (refer below), recommended until stable issuance.

Official releases of GCC and binutils may be downloaded from a GNU FTP
mirror from &lt;<a href="http://www.gnu.org/prep/ftp.html"
rel="nofollow">http://www.gnu.org/prep/ftp.html</a>&gt;. GCC snapshots
may be found at &lt;<a href="ftp://gcc.gnu.org/pub/gcc/snapshots/"
rel="nofollow">ftp://gcc.gnu.org/pub/gcc/snapshots/</a>&gt;. Binutils
snapshots may be found at
&lt;<a href="ftp://sourceware.org/pub/binutils/snapshots/"
rel="nofollow">ftp://sourceware.org/pub/binutils/snapshots/</a>&gt;.
Extract the tarballs (i.e. tar -xf filename.tar.gz) to a temporary
folders.

You can also download the latest working version using SVN & CVS. Both
source control systems are available to Cygwin via Setup, and available
to MSys in the MSys/MinGW Packages. To use them:

-   For Mingw-w64: svn co
    <https://mingw-w64.svn.sourceforge.net/svnroot/mingw-w64> mingw-w64
-   For GCCs latest development snapshot (4.5.0): svn checkout &lt;svn:
    gcc.gnu.org="" svn="" gcc="" trunk=""&gt; gcc45x or for GCC 4.4.x:
    svn co &lt;svn: gcc.gnu.org="" svn="" gcc="" branches=""
    gcc-4\_4-branch=""&gt; gcc44x
-   For Binutils latest development snapshot (2.20.51): cvs -z9
    -d:pserver:anoncvs@sourceware.org:/cvs/src co binutils or for
    binutils-2.20 stable branch: cvs -z9
    -d:pserver:anoncvs@sourceware.org:/cvs/src co -r
    binutils-2\_20-branch binutils (a directory named 'src' will be
    created and will hold the sources for either of the cases.)

### Build type options

<a href="../BTYOPT" class="alink notfound">[BTYOPT]</a>

When building binutils, GCC and Mingw-w64, you will be using standard
autotools configure scripts. It is not a good idea to build in the
source directory, so you will make a sibling directory next to the
source tree, enter it, and invoke configure with '../path/to/configure'
(which is then followed by 'make' and then 'make install'.) You will be
providing options to the configure script, in the syntax of
../path/to/configure
--flag<a href="../%3Dsetting" class="alink notfound">[=setting]</a>.
This will be further detailed below.

**Note**: Do not build GCC in the source tree or in a subdirectory
contained in source tree. This generally applies to many other autotools
based packages too, unless specifically specified by the package
developers or maintainers.

You have two main choices to make building the cross-compiler toolchain:

1\) To build with default standard multilib (allows for building to a
32-bit alternate target, using Mingw-w64's lib32), or to disable
multilib. Multilib is installed by default, if you don't want it, you
have to explicitly disable it by passing --disable-multilib to
configure, i.e.

> ../path/to/configure --disable-multilib

2\) Using standard settings of configure, which installs to /usr/local
and requires no setting changes, or to build to a sysroot you designate.
/usr/local is universally used as the default install point, and you may
wish to keep all the Mingw-w64 (64-bit) in a separate sysroot instead.
In the example in these instructions, the sysroot is '/mypath'. To use a
sysroot, pass --with-sysroot=/mypath and --prefix=/mypath as configure
flags, i.e.

> ../path/to/configure --with-sysroot=/mypath --prefix=/mypath

## Building binutils cross toolchain

<a href="../CRSBNT" class="alink notfound">[CRSBNT]</a>

Step 1) Create a build directory (e.g. 'build'), where binutils compiled
object files will be stored. Then enter into it.

Step 2) Run configure.

> For multilib:
>
> > ../path/to/configure --target=x86\_64-w64-mingw32 \\  
> > --enable-targets=x86\_64-w64-mingw32,i686-w64-mingw32
>
> For non-multilib:
>
> > ../path/to/configure --target=x86\_64-w64-mingw32 \\  
> > --disable-multilib
>
> If using a sysroot, add "--with-sysroot=/mypath --prefix=/mypath" to
> your configure command, i.e., for multilib:
>
> > ../path/to/configure --target=x86\_64-w64-mingw32 \\  
> > --enable-targets=x86\_64-w64-mingw32,i686-w64-mingw32 \\  
> > --with-sysroot=/mypath --prefix=/mypath

Step 3) Run make (type 'make'). This will take a while.

Step 4) Run make install (type 'make install')

Step 5) You may optionally delete the "build" directory to save disk
space.

Step 6) If you are using "--prefix" to install binutils to a directory
not in your $PATH environmental variable, you should add the "bin"
directory to you $PATH, i.e., for binutils installed to
/home/luser/mingw64, use the following command to make new cross
binutils visible by issuing:

> export PATH="$PATH:/home/luser/mingw64/bin"

This step is required for building GCC later.

## Install the Mingw-w64 header set and create required symlinks

<a href="../HDRSYM" class="alink notfound">[HDRSYM]</a> Step 1) The
source directory for the headers can be
mingw-w64/trunk/mingw-w64-headers, or mingw-w64/mingw-w64-headers
depending on your source.

Step 2) Create another "build" directory, and enter it.

> To install the headers, run:
>
> > ../path/to/configure --build=&lt;your build machine&gt; \\  
> > --host=x86\_64-w64-mingw32 --prefix=/mypath
>
> Then run "make install" to install the headers.

NOTE: For v3 (trunk as of writing, you MUST append x86\_64-w64-mingw32
to your prefix, such as --prefix=/mypath/x86\_64-w64-mingw32  
NOTE: You MUST also do this for the CRT

Step 3) GCC requires the x86\_64-w64-mingw32 directory be mirrored as a
directory 'mingw' in the same root. So, if using configure default
/usr/local, type:

> ln -s /usr/local/x86\_64-w64-mingw32 /usr/local/mingw
>
> or, for sysroot, type:
>
> > ln -s /mypath/x86\_64-w64-mingw32 /mypath/mingw

Step 4) Manually create the x86\_64-w64-mingw32/lib directory:

> mkdir -p /usr/local/x86\_64-w64-mingw32/lib
>
> or, for sysroot:
>
> > mkdir -p /mypath/x86\_64-w64-mingw32/lib
>
> If it already exists and you get an error, ignore it.

Step 5) Symlink x86\_64-w64-mingw32/lib directory as
x86\_64-w64-mingw32/lib64:

> ln -s /usr/local/x86\_64-w64-mingw32/lib
> /usr/local/x86\_64-w64-mingw32/lib64
>
> or, for sysroot:
>
> > ln -s /mypath/x86\_64-w64-mingw32/lib
> > /mypath/x86\_64-w64-mingw32/lib64

Note: On Windows systems or other systems that do not support UNIX type
softlinks, you may copy the entire directory to mirror it. It will have
the same effect as a symlink.

Note: The header-set and crt contains the standard-c and the windows
platform headers. Therefore it is not necessary to install an additional
package.

## Building the GCC core cross-compiler(s)

<a href="../BDGCOR" class="alink notfound">[BDGCOR]</a>

There are no GCC patches required anymore. We keep up with GCC and get
any fixes applied upstream.

Step 1) Enter into the GCC root folder and generate a folder within
(e.g. 'build'), then enter it.

Step 2) Run configure.

> For multilib:
>
> > ../path/to/configure --target=x86\_64-w64-mingw32
> > --enable-targets=all
>
> To disable multilib:
>
> > ../path/to/configure --target=x86\_64-w64-mingw32 --disable-multilib

**Note**: Remember to add the --prefix=/mypath and
--with-sysroot=/mypath flags to match the binutils build if you are
using a sysroot.

Step 3) Type 'make all-gcc'. This will build the GCC core.

Step 4) Type 'make install-gcc'. This will install the GCC core.

Step 5) You can leave the "build" directory alone for now, so you can
resume building the rest of GCC later after installing the CRT.

Now the core stuff of GCC is present and we can build the crt itself.

## Building the crt (Mingw-w64 itself)

<a href="../BLDCRT" class="alink notfound">[BLDCRT]</a>

Step 1) Create a new "build" directory for the crt. Enter the "build"
directory.

Step 2) Run configure.

> For multilib:
>
> > ../path/to/configure --host=x86\_64-w64-mingw32 --enable-lib32
> > (NOTE: This won't work if you disabled multilib!)
>
> Without multilib:
>
> > ../path/to/configure --host=x86\_64-w64-mingw32
>
> If using sysroot/prefix, again add the the --prefix=/mypath and
> --with-sysroot=/mypath flags.

NOTE: For v3 (trunk as of writing, you MUST append x86\_64-w64-mingw32
to your prefix, such as --prefix=/mypath/x86\_64-w64-mingw32 NOTE: You
MUST also do this for the HEADERS

Step 3) Type make. This will take a while.

Step 4) Type make install

> If you are performing this action on a system where sudo is used, the
> **sudo make install** may fail with an error about being unable to
> find x86\_64-w64-mingw32-ranlib, because the PATH environment variable
> is not passed along to the root user.
>
> You can work around this issue by creating a simple shell script in
> your build directory which updates PATH to include the location of
> x86\_64-w64-mingw32-ranlib, e.g.:
>
> <table class="codehilitetable">
> <colgroup>
> <col style="width: 50%" />
> <col style="width: 50%" />
> </colgroup>
> <tbody>
> <tr class="odd">
> <td class="linenos"><div class="linenodiv">
> <pre><code>1
> 2
> 3</code></pre>
> </div></td>
> <td class="code"><div class="codehilite">
> <pre><code>#!/bin/sh
> export PATH=&quot;$PATH:/usr/local/bin&quot;
> make install</code></pre>
> </div></td>
> </tr>
> </tbody>
> </table>
>
> Then call that script with sudo instead.

Step 5) Make sure you have the following directories in the directory
you have installed the mingw-w64 toolchain to:

    <root>/x86_64-w64-mingw32
    <root>/x86_64-w64-mingw32/include
    <root>/x86_64-w64-mingw32/lib
    <root>/x86_64-w64-mingw32/lib32
    <root>/x86_64-w64-mingw32/lib64 [link to lib]
    <root>/mingw [link to x86_64-w64-mingw32]
    <root>/mingw/include
    <root>/mingw/lib
    <root>/mingw/lib32
    <root>/mingw/lib64 [link to lib]

If you are using MSys/MinGW on Windows, remember to copy the "linked"
directories to simulate the use of a symbolic link.

Note: For non-multilib builds, you can omit the "lib32" and "lib64"
directories and only have "lib".

Note: Currently there are no dlls built. As long as we use static crt
import libraries we won't need a ctor/dtor dll (mingwm10.dll).

## Finishing GCC (the libraries built using GCC core and Mingw-w64)

<a href="../FNSHGC" class="alink notfound">[FNSHGC]</a>

Now you are ready to build the rest of GCC:

Step 1) Enter back into your GCC "build" directory.

Step 2) Type 'make'. This will take a while.

Step 3) Type 'make install'

## Path update and using your new cross-compiler

<a href="../PTHUPD" class="alink notfound">[PTHUPD]</a>

Permanently update your path to use your new cross-compiler:

The binaries are all prefixed with the Mingw-w64 triplet
x86\_64-w64-mingw32-, so there are no file name clashes.

-   If you are using Cygwin or \*nix, you will add the directory to your
    path in .bashrc in your home directory (the file may be hidden).
-   If you are using MSys, you will need to add the directory to your
    path in /etc/profile.
-   To reiterate, for default /usr/local, add /usr/local/bin to your
    PATH (this should not be necessary.) If using a sysroot, add
    /mypath/bin to your path.

You are finished.

To use your cross-compiler, simply use --host=x86\_64-w64-mingw32 as a
configure option. Be sure to -I/usr/local/include or -I/mypath/include
and -L/usr/local/lib or -L/mypath/lib to your CFLAGS to link your
builds.

Often you must --enable-shared if you want DLLs as opposed to static
libs, but it is not always the case.

Simply use the -mwindows option for windows GUI applications. By
default, -mconsole is used and produce console applications. Also, you
can use the -mdll option for generating shared objects (dll), however
normal gcc/g++ with the -shared flag or a proper ld (linker) command
will do this.