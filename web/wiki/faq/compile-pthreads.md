# Compile pthreads

POSIX 1003.1-2001 standard defines an application programming interface
(API) that is more commonly known as *pthreads*. Windows (32b or 64b)
does not implement the standard. For convenience a wrapper library
called pthreads-win32 implements most of the functions defined in the
standard. The library is available at
<a href="http://sourceware.org/pthreads-win32/"
rel="nofollow">http://sourceware.org/pthreads-win32/</a>.

As the name tells, the library is not directly 64bit compatible. To
compile with pthreads you need first to obtain working version of it.
(NB that with 2.9.0 it might be 64bit compatible now, without patches).

## Getting binary

There should exist a pre-build binary, that is they easiest way to get
pthreads support. At the moment it can be found from [sourceforge
mingw64
files](https://sourceforge.net/projects/mingw-w64/files/External%20binary%20packages%20%28Win64%20hosted%29/pthreads/).

## Compiling pthreads

1\) Download latest CVS version from the pthreads-w32 page, or use cvs
directly:

    cvs -d :pserver:anoncvs@sourceware.org:/cvs/pthreads-win32 checkout pthreads

2\) Download pthreads-w32 patch from mingw-w64 svn under directory like
'experimental/patches/pthreads'
[Link](http://mingw-w64.svn.sourceforge.net/viewvc/mingw-w64/experimental/patches/pthreads_win32/).
Currently (06-09-2010) the experimental-new-w64sup.patch works.

3\) Apply the patch (depending on where have you put the stuff but
something like this)

    patch -p0 < experimental-new-w64sup.patch

4\) Compile the pthreads. The makefile is patched so the 'CROSS=' wont
work. You need to modify GNUmakefile, so that you have line like

    target  = x86_64-w64-mingw32

in the makefile. Add correct target here. You need to also produce
pthreads\_win32\_config.h from config.h by

    config.h pthreads_win32_config.h

After this you can compile the library:

       make clean GC

5\) Now you have .dll that you can use with ready binaries, and
pthreads.a that provides libpthread.a (placed in correct directory) and
headers pthread.h sched.h sched.h that might be needed when compiling
with pthread support. You can also compile this library so it can be
statically linked, but then you need non-portable code in the program
using pthreads. See pthreads readme for more information.

If any of these steps fail, you might find [Email list
archive](http://www.mail-archive.com/mingw-w64-public@lists.sourceforge.net/msg00900.html)
use full.

## Using pthreads

Place the header files (*.h) to somewhere where your compiler can find
them. Project specific works as well as system or mingw64 include
directory. Place libraries (*.a) again where your compiler can find
them, for example project directory or mingw64 lib directory. When you
have ready .exe you need to place pthreads.dll to correct place, either
windows system folder or same folder as the .exe. If you want to compile
static binary (no dll needed), you need to compile pthreads by yourself,
see above.