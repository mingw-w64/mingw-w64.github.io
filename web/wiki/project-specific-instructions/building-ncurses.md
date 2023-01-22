# Building NCurses with mingw-w64

NCurses is a shell library that provides console abstraction, ...

## Download unavailable

There is no prebuilt binary available yet. See below for build
instructions

## How to Build

-   set up mingw-w64: [GeneralUsageInstructions](../general-usage-instructions.md)

-   set up MSYS: [MSYS](../msys.md)

-   get NCurses (v5.9 at the time of writing):
    <a href="http://ftp.gnu.org/pub/gnu/ncurses/"
    rel="nofollow">http://ftp.gnu.org/pub/gnu/ncurses/</a>

-   in the source directory from the MSYS shell:

        configure --host=x86_64-w64-mingw32 --enable-term-driver --enable-sp-funcs --prefix=/some/prefix

-   type

        make
        make check
        make install