# Creating a native Win64 compiler

To create a native Windows x86-64 compiler you first have to create a
MinGW-w64 cross compiler.

Once the cross compiler is created, you can start creating a native
windows compiler. Just use the same MinGW-w64 source that was used for
creating the cross compiler. First of all, a native version of binutils
must be created.

It is good practice to use a prefix for building the native compiler.
Therefore these instructions will assume that the native compiler will
be installed in a custom directory instead of the default `/usr/local`.

## Make sure the cross compiler can be found

The path to the cross compiler binary should be in your `PATH` variable.
If the cross compiler was build without a prefix and the
`--with-sysroot` options, the binary is installed in `/usr/local/bin`
and that directory is probably already available in your `PATH` (this
can be checked with typing: `echo $PATH`). If the cross compiler was
installed in another directory and that directory was not added to the
`PATH` environment variable before, you can do this now by typing:

`PATH=$PATH:<prefix>/bin; export PATH`

Replace `<prefix>` with the variable for `--prefix` and `--with-sysroot`
you used when building the cross compiler.

## Building native Win64 binutils

Enter the source directory of binutils in the MinGW-w64 source package.
This should be located in `binutils/src`. Create a new directory in
which the build process will be performed. Do not use the same build
directory you have used for creating the cross compiler, make a new one
instead. Enter the generated build directory.

Binutils must now be configured with the appropriate options. This can
be done by typing:

`../configure --host=x86_64-w64-mingw32 --target=x86_64-w64-mingw32 --prefix=<prefix> --with-sysroot=<prefix>`

Other configure paramaters that are important are:

-   `--enable-targets=x86_64-w64-mingw32,...` (when using multilib)
-   `--disable-multilib` (when not using multilib)

After `configure` has finished type:

`make`

And thereafter:

`make install`

## Make a 'winsup' directory

Before you can start the building process a `winsup` directory is
necessary in the gcc root directory. Enter the `gcc/gcc` directory of
the mingw-w64 source package and create a `winsup/mingw/` directory.
Enter this directory and create a symlink to the `include` directory of
your cross compiler:

`ln -s <cross compiler prefix>/x86_64-w64-mingw32/include include`

An alternative option is to copy the `include` directory:

`cp -r <cross compiler prefix>/x86_64-w64-mingw32/include include`

## Copy system headers

The `include` directory with the system headers must also be available
in the `<prefix>/mingw` and `<prefix>/<target>` directory. Therefore,
install the headers with the following commands:

    /path/to/mingw-w64-headers/configure --prefix=<prefix> --build=x86_64-w64-mingw32 --host=x86_64-w64-mingw32
    make
    make install

NOTE: As of v3 (Trunk as of writing), you must use append your
architecture to the prefix, such as using
--prefix=&lt;prefix&gt;/x86\_64-w64-mingw32

Making `gcc` relies on an ordinary `mingw` (instead of
`x86_64-w64-mingw32`) directory. Therefore a symlink can be made so that
the `mingw` directory can be found. At the same time, also create a
symlink from the `lib` directory to the `lib64` directory:

    ln -s <prefix>/x86_64-w64-mingw32  <prefix>/mingw
    ln -s <prefix>/x86_64-w64-mingw32/lib <prefix>/x86_64-w64-mingw32/lib64

When you are building in an environment that doesn't support symlinks
(mingw itself for example), but instead copies the directories, make
sure the `lib64` directory is copied as well in the `<prefix>/mingw`
directory. If unsure, check if a `<prefix>/mingw/lib64` directory is
available. If it isn't copy the `<prefix>/mingw/lib` directory to
`<prefix>/mingw/lib64`.

## Building gcc

Now everything is setup to configure the gcc build. Go to the gcc root
directory in the MinGW-w64 source package, this should be located in
`gcc/gcc`. Create a new directory in which building gcc will be
performed. Make sure you use another build directory than the one used
when building the cross compiler. Enter the generated build directory.

Some important gcc configuration options to consider are listed below:

-   `--enable-targets=all` (when using multilib)
-   `--disable-multilib` (when not using multilib)
-   `--enable-languages=[c,c++,objc,obj-c++,fortran,java,ada]`
-   `--enable-fully-dynamic-string` This option affects libstdc++ ABI
    and allows (among other things) empty `std::string` objects to be
    passed across DLL boundaries. This is enabled by default for GCC
    4.7+
-   `--disable-werror` (try this option if you experience an error
    during stage 2 of the gcc bootstrapping process)
-   `--disable-shared` Using this your compiled programs won't need the
    `libgcc_s_sjlj-1.dll` library (otherwise you have to put it in the
    same directory as the executable, or at least make sure it is
    accessible from your `$PATH` environment variable).

For a complete list of configuration options see:
<a href="http://gcc.gnu.org/install/configure.html" rel="nofollow">gcc
configuration options</a>.

If you encounter problems, it might be a good idea to limit the enabled
languages to the languages you need gcc for. It might be the case that
you are missing some prerequisites for a specific (default enabled)
language.

Configure gcc by typing:

`../configure --host=x86_64-w64-mingw32 --target=x86_64-w64-mingw32 --prefix=<prefix> --with-sysroot=<prefix>`

You might have to set the appropriate `include` and `lib` directories as
well by providing the `CFLAGS` to configure:

`../configure CFLAGS="-I/<cross compiler prefix>/include -L/<cross compiler prefix>/lib" ...`

Replace `<cross compiler prefix>` with the variable you used for
`--prefix` and `--with-sysroot` when building the cross compiler.

If you want to make a configure without refering to previously build
cross-compiler's internal directories, you need to do for it the same
steps as for a cross-compiler. First build gcc's bootstrap by 'make
all-gcc' and 'make install-gcc'. Then make sure that crt is installed in
new-sysroot, too. Then you can re-enter gcc's build directory and do
'make clean' and continue with this next step.

After gcc is configured, start the 3 stage bootstrapping process that
creates the native Win64 gcc compiler:

`make`

And once `make` has finished:

`make install`

This should complete your gcc installation.

## Building the CRT

To use the compiler the C Run Time should be build as well. Another
option is to copy the files from the cross compiler build. Go to the
`<prefix>/x86_64-w64-mingw32/lib` directory of your native compiler and
copy the files from your cross compiler:

`cp <cross compiler prefix>/x86_64-w64-mingw32/lib/* .`

The method in this section probably can be replaced with something
better. But for now this should work.

## Applying patches

Mingw-w64 is under constant development. When using the daily source
snapshots, it might be the case that a patch for gcc is necessary to
make it work. If you encounter a problem building a native Win64
compiler, there is a good chance somebody in the Mingw-w64 irc channel
is able to help you, or tell you whether a patch is necessary or not. If
a patch must be applied to gcc, proceed in the following way:

-   get the patch and put the code in a file of your choice
-   go to the `<source>/gcc/gcc` directory and type:

`patch --strip=1 -i <patch filename>`

-   if applying the patch succeeds, you should see output similar to
    this:

          patching file <file 1>
          patching file <file 2>
          ...
          patching file <file n>