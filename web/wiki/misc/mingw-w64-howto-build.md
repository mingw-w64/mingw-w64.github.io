# mingw-w64-howto-build

## HowTo build x86\_64-pc-mingw32 cross-compiler

Date / Version / Author  
2007-07-31 1.0 Kai Tietz &lt;Kai.Tietz at onevision.com&gt;  
2007-08-20 1.1 Kai Tietz &lt;Kai.Tietz at onevision.com&gt;  
2007-08-21 1.2 NightStrike &lt;nightstrike at gmail.com&gt;  
2007-10-01 1.3 NightStrike &lt;nightstrike at gmail.com&gt;  
2007-11-27 1.4 NightStrike &lt;nightstrike at gmail.com&gt;  
2008-11-21 1.5 Kai.tietz at onevision.com  
2009-04-29 1.6 Kai.tietz at onevision.com

This document describes how to build the amd64 mingw32 gcc toolchain as
a cross-compiler on cygwin and unix shells. The same documentation can
be used for 32-bit of this runtime. For this simply exchange the triplet
x86\_64-pc-mingw32 by i686-pc-mingw32.

**0. Requirements**  
On a clean cygwin install, you will need the following additional
packages installed:

-   A complete gcc toolchain for the host system
-   bison
-   cvs
-   diffutils
-   flex
-   gmp
-   make
-   mpfr
-   perl (for pod2man)
-   subversion
-   wget

**1. Download packages**  
The following packages you need to download  
- binutils 2.19 or newer.  
- gcc version 4.4 or newer.  
- current mingw-w64-snapshot available at
<https://sourceforge.net/projects/mingw-w64>

Now extract these tarballs to a temporary folder. E.g. use ~/w64src. For
the tarballs with  
extension .tar.gz or .tgz use the following command to extract : tar
-xzf &lt;tarball&gt;'. For  
tarballs with extension .tar.bz2 or .tbz2 use the command 'tar -xjf
&lt;tarball&gt;'.  
There are now three folders within you temporary folder: trunk,
binutils, and gcc.

**2. Build type options**

You have at least two different choices to build the crosscompiler
toolchain:  
I) Using standard settings of configure.  
II) Using --prefix and --with-sysroot configuration

I assume that '/usr/local/' is the &lt;install-root&gt; for build type
I, the path specified using --with-sysroot is  
the root for type II. For this example, it will be set to '/mypath'.

**3. Building binutils cross toolchain:**  
Step 1) Enter into the binutils root folder and generate a folder within
(e.g.  
'build'). Then enter into it.  
Step 2 for I) Type '../configure --target=x86\_64-pc-mingw32'  
Step 2 for II) Type '../configure --target=x86\_64-pc-mingw32
--prefix=/mypath --with-sysroot=/mypath'.  
Step 3) Type 'make'  
Step 4) Type 'make install'

Now copy the content of the folder 'trunk/mingw-w64-headers/include'
into your '&lt;install-root&gt;/x86\_64-pc-mingw32/include'  
folder. If you choose the configuration variant II create in /mypath a
symbolic link named  
'mingw' pointing to the directory 'x86\_64-pc-mingw32'. For instance:  
$ cd /mypath  
$ ln -s x86\_64-pc-mingw32 mingw

**4. Building the gcc core cross-compiler(s):**  
Step 0) If you have to patch gcc, may do this here. There are some
patches necessary, if you want  
to cross compile libiberty with early header sets, or if you want to use
gfortran. These patches  
are available by the 'gcc-patches' mailing list at 'gcc.gnu.org' or by
taking a look at mingw.org  
or mingw-w64 sites.  
Step 1) Enter into the gcc root folder and generate a folder within
(e.g. 'build'). Then you may  
apply optional patches to gcc (currently there is a patch file for gcc
needed to fix some  
problems about autoimported variables, libiberty and the fortan
compiler). Enter into the  
build directory when finished.  
Step 2 for I) Type: '../configure --target=x86\_64-pc-mingw32'.  
Step 2 for II) Type: '../configure --target=x86\_64-pc-mingw32
--prefix=/mypath --with-sysroot=/mypath'.  
Step 3) Type 'make all-gcc'  
Step 4) Type 'make install-gcc'

Now the core stuff of gcc is present and we can build the crt itself.

**5. Building the crt:**  
Step 0) If you are using variant II, may you need to adjust the 'prefix'
value in Makefiles.  
Step 1) Enter into the trunk/mingw-w64-crt root directory.  
Step 2 for I) Type '../configure --host=x86\_64-pc-mingw32'  
Step 2 for II) Type '../configure --host=x86\_64-pc-mingw32
--prefix=/mypath --with-sysroot=/mypath'  
\_(If you are building the 32-bit toolchain, please add to configure the
options --disable-lib64 --enable-lib32)  
Step 3) Type 'make'  
Step 4) Type 'make install'  
Note: Currently there is no dll build. As long as we use static crt
libraries.we won't need a ctor/dtor dll.

**6. Now you are ready to build the rest of gcc:**  
Step 1) Enter into your gcc root folder and generate a symbolic link
&quote;winsup&quote; pointing to &lt;install-root&gt;.  
Â %nbsp;For example: $ cd /mygcc  
$ ln -s /mypath winsup  
Step 2) Enter into your generated folder within your gcc root source
folder.  
Step 3) Type 'make'  
Step 4) Type 'make install'

**Some further notes**  
\_There is currently no **.DLL** build in crt. As long as we build the
crt as static library, there is no need to build a ctor/dtor DLL.

The header-set and the crt-libraries supporting Windows GUI, too. There
is no need to install a 'w32api' package, as for 32-bit mingw.

The building for Windows-GUI applications can be done by specifying to
'gcc' as command-line option '-mwindows'. By default the option
'-mconsole' is used and console applications are build. If you want to
generate shared objects (dll's') use the '-mdll' option.
