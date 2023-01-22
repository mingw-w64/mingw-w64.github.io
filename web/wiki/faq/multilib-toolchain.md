# Compiling a Multilib Toolchain

## Introduction

The multilib feature is available for 4.5 gcc version and it is still
under construction to make things round. First you should use 64-bit
defaulted compilers (target triplet x86\_64-w64-mingw32) for this, as
the 32-bit version isn't at the moment completely supported.

## First step the preparation of sys-root and building of binutils

First build binutils by the configuration options:
'--prefix=&lt;your-sysroot&gt; --with-sysroot=&lt;your-sysroot&gt;
--target=x86\_64-w64-mingw32
--enable-targets=x86\_64-w64-mingw32,i686-w64-mingw32'  
After compiling it, please install it by 'make install'.

Now enter into the &lt;sysroot&gt;/x86\_64-w64-mingw32 folder and create
here the link lib64 pointing to the lib folder here (For native windows
builds you need to use here junction points).

Now generate within your &lt;sys-root&gt; a symbolic link mingw pointing
to the directory &lt;x86\_64-w64-mingw32 (Again for windows native
please use junction points).

## Second step building gcc core compilers

Now we can build first stage of gcc. For configuration of gcc, use
configure options: '--target=x86\_64-w64-mingw32 --enable-multilib
--enable-64bit --prefix=&lt;sys-root&gt;
--with-sysroot=&lt;sys-root&gt;'  
Note: By using additionally the option
'--enable-version-specific-runtime-libs' you avoid that 32-bit and
64-bit libgcc\_s\*.dll getting override each other.

After configuration please create within the gcc's source root the link
'winsup' pointing to your &lt;sys-root&gt; directory. This is sadly
necessary as cygwin/mingw.org assumes that headers and runtime a build
in one big tree.

Now we are ready to do 'make all-gcc' and afterwards 'make install-gcc'.

## Third step building runtime

After build and install is completed, we are ready to install
runtime-crt and libraries.  
Now add to your PATH environment the folder &lt;sys-root&gt;/bin. To
configure our runtime by the options: '--host=x86\_64-w64-mingw32
--enable-lib64 --enable-lib32 --prefix=&lt;sys-root&gt;
--with-sysroot=&lt;sys-root&gt;.  
After configuration type as usual 'make' and than 'make install'.

## Fourth step building gcc's libraries

Now re-enter your gcc configuration folder and do the rest of bootstrap
by typing 'make' and 'make install'.

A three stage bootstrap isn't possible (as usual for a windows native
build, as you need to have working symbolic links, but native windows
just knows about junction points and of course the pathes used are
different between unix-shell and native windows.