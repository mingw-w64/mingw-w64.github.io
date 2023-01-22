# How to build popular projects with mingw-w64/w32

Please check the mingw-w64/w32 downloads page ([External binary
packages](https://sourceforge.net/projects/mingw-w64/files/External%20binary%20packages%20%28Win64%20hosted%29/))
for a copy of what you're looking for. If it's not there, read the
readme included in the project's source code and if you need a configure
script, read [MSYS](../msys.md). This page
contains a list of projects that need some special attention to use with
mingw-w64/w32. This is not at all a bad thing, most things work (very
well):

-   [Boost](./building-boost.md)
-   [Nokia's Qt](./building-qt.md/)
-   [OpenSSL](./building-openssl.md)
-   [NCurses](./building-ncurses.md)
-   ...

NOTE: these how-to's will assume you're using a native compiler. Those
cross-compiling from Linux should have some starting knowledge about how
to cross-compile stuff.