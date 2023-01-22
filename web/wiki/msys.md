# MSYS

## Where to get it

There are three places you can get MSYS: \* The [MinGW
project](https://sourceforge.net/projects/mingw/files/MSYS/), with
seperate packages of all official MSYS packages. Takes a long time to
download and install everything. \* The all-in-one package on the
[MinGW-w64 download
page](http://sourceforge.net/projects/mingw-w64/files/External%20binary%20packages%20%28Win64%20hosted%29/MSYS%20%2832-bit%29/).
It is updated on request (see third option for very up to date
collection) \*
[MinGW-builds](http://sourceforge.net/projects/mingwbuilds/files/external-binary-packages/)
provides an ultra-inclusive MSYS package with a bunch of additional
useful stuff.

## How to use the package

Installing MSYS is quite easy.

-   You'll need to download the above package.

-   Unzip it somewhere, for example C:\\msys so that C:\\msys\\bin
    contains (among others) bash.exe.

-   doubleclick (or make a handy shortcut and run that) on
    C:\\msys\\msys.bat.

-   type

        sh /postinstall/pi.sh

-   answer the friendly questions and you're all set up.

## Mingw-w64/w32 specifics

When running an autotools configure script, these options will come in
handy:

-   for a 64-bit build: --host=x86\_64-w64-mingw32
-   for a 32-bit build: --host=i686-w64-mingw32

If you are experiencing problems, you can also set --build to the same
value. Some configure scripts also use --target instead of --host. Use
configure --help to get all possible options.

### --host, --target, and --build explained

--host specifies on what platform/architecture the compiled program is
going to run. --target specifies the platform/architecture that the
program should be configured for and will be compiled for. This should
only have effect when building cross-compilers. --build specifies the
platform/architecture the build process is going to be executed.

## What is MSYS

MSYS is a Minimal SYStem, providing several crucial unix utilities under
a compatibility layer (the msys-1.0.dll file). MSYS should provide
everything to make compilation of common GNU software. An outdated
<a href="http://mingw.org/wiki/MSYS" rel="nofollow">description</a> by
the makers themselves.

### MSYS provided by the mingw-w64/w32 project

This package is not more than a collection of the 50+ packages provided
by mingw.org. It was created as a (huge) convenience to our users, to
let them be productive instead of downloading every part seperately. The
accompanying sources are also provided and can be found in the same
download section as mentioned above.

This package is 32-bit, but will run flawlessly on x64 Windows. There
will never be a 64-bit native MSYS (is there any need?) because the only
compiler capable of building MSYS applications is the outdated gcc
3.4.4, which does not support x64 native Windows targets.