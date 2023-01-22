# Building Boost

## Building Boost with MinGW-W64

### Building on Windows

#### Download

You will require the following software:

-   MinGW-w64 Toolchain ([from
    here](https://sourceforge.net/projects/mingw-w64/files/))
    -   for 32bit hosts targeting
        [32bit](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/sezero_20110510/mingw-w32-bin_i686-mingw_20110510_sezero.zip/download)
        or
        [64bit](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/sezero_20110510/mingw-w64-bin_i686-mingw_20110510_sezero.zip/download)
    -   for 64bit hosts targeting
        [64bit](http://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/sezero_20110510/mingw-w64-bin_x86_64-mingw_20110510_sezero.zip/download)
-   Boost Sources ([from
    here](https://sourceforge.net/projects/boost/files/boost/))
    -   for example
        [boost\_1\_46\_1.7z](http://sourceforge.net/projects/boost/files/boost/1.46.1/boost_1_46_1.7z/download)

Optionally:

-   Perl (<a href="http://www.activestate.com/activeperl/downloads/"
    rel="nofollow">from here</a>)
    -   May not be required.
-   Boost Jam Sources ([from
    here](http://sourceforge.net/projects/boost/files/boost-jam/))
    -   for example
        [boost-jam-3.1.18.zip](http://sourceforge.net/projects/boost/files/boost-jam/3.1.18/boost-jam-3.1.18.zip/download)
    -   Or you can simply use the bjam from the Boost Sources

#### Install

Install Active Perl (which may not be required).

#### Extract

Extract the boost, boost-jam and mingw-w64 archives somewhere.  
These instructions are written with the following layout:

    c:\
       mingw\
             mingw32 (32bit mingw-w64 toolchain containing bin, include, etc)
             mingw64 (64bit mingw-w64 toolchain containing bin, include, etc)
       src\
           boost_1_46_1 (containing boost, doc, libs etc)
           boost-jam-3.1.17 (containing boehm_gc, images, etc)

#### 32bit Build

Add the tools to the PATH

    set PATH=c:\mingw\mingw32\bin;%PATH%

Compile Boost-Jam

    c:
    cd \mingw\src\boost-jam-3.1.18
    build.bat gcc

Compile Boost

    c:
    cd \mingw\src\boost_1_46_1
    ..\boost-jam-3.1.18\bin.ntx86\bjam.exe --prefix=c:\mingw\boost32 ^
    toolset=gcc address-model=32 variant=debug,release link=static,shared ^
    threading=multi  install

You will now have a c:\\mingw\\boost32 directory containing the boost
headers and libs :-)

#### 64bit Build

Add the tools to the PATH

    set PATH=c:\mingw\mingw64\bin;%PATH%

Compile Boost-Jam  
(you can use the 32bit version instead if you compiled it already)

    c:
    cd \mingw\src\boost-jam-3.1.18
    build.bat gcc

Compile Boost (If using the 32bit bjam.exe, Make sure you use the
correct path)

    c:
    cd \mingw\src\boost_1_46_1
    ..\boost-jam-3.1.18\bin.ntx86_64\bjam.exe --prefix=c:\mingw\boost64 ^
    toolset=gcc address-model=64 variant=debug,release link=static,shared ^
    threading=multi  install

(You might have to add `define=BOOST_USE_WINDOWS_H` to the parameter
list.)

You will now have a c:\\mingw\\boost64 directory containing the boost
headers and libs :-)

#### Notes

You will see several message regarding python which should be safe to
ignore.  
You will see some message stating that 64bit is not supported for some
parts of boost. If these are parts you need you should contact boost for
support.

If you have instructions for cross compiling boost from linux, Please
contact the mingw-w64 mailing list to get this page updated.
