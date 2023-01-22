# DOWNLOADS: What do I want

Welcome to mingw-w64 file download information.  
This page should leave you all knowing of the filenames under the
[SourceForge files](http://sourceforge.net/projects/mingw-w64/files/)
section and what's in them.

## Filename Format

The toolchain file names are made up of sections.  
Examples :  
mingw-w32-bin\_i686-cygwin-1.5.25-15\_20100123.tar.bz2  
mingw-w64-1.0-bin\_x86\_64-linux\_20100226.tar.bz2  
mingw-w32-bin\_x86\_64-linux\_20100223\_sezero.tar.gz  
The format is:  
&lt;Target&gt;<a href="../-Version" class="alink notfound">[-Version]</a>-&lt;Src/Bin&gt;-&lt;Host&gt;<a href="../-Cygwin%20Version" class="alink notfound">[-Cygwin
Version]</a>\_&lt;Date
Code&gt;<a href="../_personal%20tag" class="alink notfound">[_personal tag]</a>.<a href="../extension" class="alink notfound">[extension]</a>

### &lt;Target&gt;

"mingw-w32" or "mingw-w64"  
The target is the binary format the tool chain will generate.  
"mingw-w64" means the toolchain will generate 64bit binaries that will
run on windows natively (64bit windows required)  
"mingw-w32" means the toolchain will generate 32bit binaries that will
run on windows natively  
In the SourceForge? file area for the mingw-w64 project, please take
note of the groups titled

-   Toolchains targetting Win32
-   Toolchains targetting Win64

### <a href="../-Version" class="alink notfound">[-Version]</a>

Currently either "-1.0" or missing.  
This is an optional tag that indicates the released version of the
mingw-w64 CRT/Headers that the toolchain was built with.  
If it's missing then the toolchain was build from the svn trunk  
otherwise it was build from the latest releases at the time.

### &lt;Src/Bin&gt;

This tag indicates whether the download is just source code or compiled
binaries.  
If you want a something you can run, you'll want "-bin-"

### &lt;Host&gt;

"i686-cygwin" or "i686-mingw" or "i686-darwin" or "x86\_64-linux" or
"i686-linux"  
This is the type of host that the toolchain you are downloading will run
on. If you are working in 32bit linux, you'll need the "i686-linux"
one.  
If you are working in windows command prompt you will want
"i686-mingw"  
and so on.

### <a href="../-Cygwin%20Version" class="alink notfound">[-Cygwin
Version]</a>

An optional tag stating the of the cygwin dll that the toolchain was
built with  
Its only applicable for toolchains that run on cygwin  
NOTE : The 1.5 version have been known to run in the 1.7 version of
cygwin.

NOTE2 : The Cygwin setup repository also provides mingw64-x86\_64 and
mingw64-i686 respectively for 64bit and 32bit targets.

NOTE3 : You do not require a win64 machine to use the 64bit target
compilers, since it is Cygwin (32bit) hosted.

### &lt;Date Code&gt;

A code which represents the date the file was generated.  
It's in the format YYYYMMDD. If today were the 2nd of March, 2010 the
date code would be 20100302.

### <a href="../_personal%20tag" class="alink notfound">[_personal tag]</a>

This is an optional tag that is used to distinguish personal builds from
automated builds.  
An example of this is the build done by sezero. They are postfixed with
"-sezero"

### <a href="../extension" class="alink notfound">[extension]</a>

This is the compressed archive file extension.  
"tar.bz2" - A tar archive compressed with bzip2  
".zip" - A zip file compressed with zip that can be extracted with
windows built-in zip program
(<a href="http://www.7-zip.org/" rel="nofollow">7zip is MUCH faster</a>)

## What do you want

What you will want to download depends on what you want to do with it.

Here are some steps to help you

1\) What platform or host type are you building on:  
In other words this is the platform of the host that you will be running
the compiler on.  
The answer to this question will help you select the value for the
&lt;host&gt; tag.

2\) Do you want to generate 32bit or 64bit windows binaries?  
The answer to this will help you select a value for the &lt;target&gt;
tag.

3\) Would you like a toolchain built with released version of source or
built from the source trunks?  
The answer to this will help you choose the
<a href="../-Version" class="alink notfound">[-Version]</a> tag

4\) Would you like a prefixed (g++ = bin/g++.exe) or non-prefixed
toolchain? Prefixed means the command you run for g++ will be
bin/i686-w64-mingw32-g++.exe (for the 32bit toolchains)  
Non-Prefixed means the command you run for g++ will be bin/g++.exe  
All of the automatically built toolchains are prefixed and the sezero
toolchains (under personal builds) are not prefixed. You can turn a
prefixed toolchain into a non-prefixed toolchain by renaming the
prefixed files in the bin directory and removing the prefix. Another
option is to create symbolic links to the prefixed binaries; an option
available in Windows Vista and above using "mklink.exe". For example,
"mklink gcc-4.5.2.exe x86\_64-w64-mingw32-gcc-4.5.2.exe" will create a
symbolic link named gcc-4.5.2.exe which points to
x86\_64-w64-mingw32-gcc-4.5.2.exe in the same working directory. You can
create most of them using a FOR loop, such as
`FOR /F "usebackq tokens=4 delims=-" %i IN (`dir
^\*.exe`) DO mklink %i x86_64-w64-mingw-%i`.

You should now be well on your way to compiling for windows 32bit/64bit
:-)

## What's in the downloads

Put simply, they are toolchains that generate binaries for 32bit or
64bit windows, but there are many toolchains that can them selves run on
several non-windows hosts. Don't let this confuse you as they all will
still generate binaries for either 32bit or 64bit windows.

The mingw-w64 project maintains a C interface to msvcrt.dll that allow
GNU GCC to run on and build for native windows

GCC is the compiler used with the mingw-w64 C interface to msvcrt.dll
and facilitates cross compiling to native
windows.<a href="../BR" class="alink notfound">[BR]</a>\] Cross
compiling is where your compiler is running on one platform (say linux)
and you are compiling programs that run on another (say windows).  
Similarly a native compiler is where your compiler is running one
platform (say windows) and you are generating binaries for that same
platform (again windows).  
(more or less ;-)

A compiler tool chain consists of all the tools required to generate a
binary (static lib, shared lib, executable, etc). The mingw-w64 project
provides the C runtime and headers, GNU provides GCC and binutils, and
other libs that are required are provided from various other places.
These are all compiled nightly as automated builds and uploaded to
source forge. What you end up with is a compressed archive that you can
download somewhere onto your computer, extract into a new directory and
begin creating native 32bit or 64 bit binaries with. You will need to
add the "bin" directory from the archive to your path first.

All of the automated tool chain builds on SourceForge? are prefixed.
This means the binaries you find in the "bin" folder will all start with
"i686-w64-mingw32-" or "x86\_64-w64-mingw32-". This is standard for a
cross compiler as it will not interfere with the operation of the native
gcc which is not prefixed. If you're sure you don't want a prefixed tool
chain, you can strip the prefixes from all the executables in the bin
directory.

You can use prefixed toolchains with configure by specifying the host
triplet you wish to build for (EG "--host=x86\_64-w64-mingw32"). If
configure detects that you are building FOR a host that is not the same
as the one you are building ON then it will automatically search for a
prefixed compiler to use. Occasionally you will need to specify the
build option as well to force a cross compile, EG
"--build=i686-pc-mingw32 --host=i686-w64-mingw32" (i686-pc-mingw32 is
the host triplet for mingw.org compilers)

Once you have downloaded the correct toolchain for the host you are
building on and that toolchain targets the windows you want
(32bit/64bit) you can start creating windows native binaries.
