# How to use w64 native compiler in cygwin shell

The whole trick is to set C\_PLUS\_INCLUDE\_PATH and C\_INCLUDE\_PATH
**BEFORE** the cygwin.dll is translating the paths, and **NOT** from
within Cygwin.  
The mingw.bat file can be used as template and needs to be adjusted for
the location of the sysroot of the native toolchain on your system.  
Additionally, few things needs to be exported in shell:

-   export
    LIBRARY\_PATH='&lt;dos-path-to-sysroot&gt;/x86\_64-pc-mingw32/lib'
-   export
    LD\_LIBRARY\_PATH='&lt;dos-path-to-sysroot&gt;/x86\_64-pc-mingw32/lib'
-   export CPP='g:/mingw/bin/x86\_64-pc-mingw32-gcc -E'
