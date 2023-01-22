# Running the testsuite on Linux

While building a cross-compiled copy of the mingw-w64 toolchain using a
Linux host it is possible to execute the testsuites which are bundled
with binutils and gcc.

## Requirements

To run the binutils and gcc test suites you need the following:

-   A Linux environment
    -   The kernel needs to have binfmt support enabled (this enabled by
        default on all modern Linux environments)
    -   To execute the testsuite for the Win64 target you need to have a
        x86\_64 based Linux environment
-   DejaGNU
    -   The binutils and gcc testsuites need DejaGNU to run all
        individual tests
-   Wine
    -   To perform tests for the Win32 target you need to have the 32bit
        version of wine installed
    -   To perform tests for the Win64 target you need to have the 64bit
        version of wine installed
    -   binfmt needs to be configured so that .exe binaries are
        automatically executed by wine
-   Mingw-w64 headers and crt
    -   For win32 the following sysroot needs to be used:
        /usr/i686-w64-mingw32/sys-root
    -   For win64 the following sysroot needs to be used:
        /usr/x86\_64-w64-mingw32/sys-root

## Limitations

At the moment it is necessary that the Linux kernel has binfmt support
enabled and that it is configured to execute .exe binaries using wine.
As this is not the case on certain environments (like the Fedora Linux
<a href="http://koji.fedoraproject.org/koji/" rel="nofollow">Koji
package build system</a>) it would be nice to adjust the DejaGNU
configuration so that it automatically uses wine to execute .exe
binaries instead of relying on the binfmt kernel feature to call wine
under the hood.

When this limitation is resolved it will become possible to
automatically run the testsuite whenever a new cross-compiled gcc
package is built on clean build environments (like the Fedora koji
builders) and make it more easy to share the testsuite results with the
gcc developers.

If you're familiar with DejaGNU and know how to make it test binaries
using wine feel free to contact epienbro on \#mingw-w64

## Preparing a wine prefix

To run the testsuite it is recommended to generate a clean wine prefix.
After the testsuite is completed this wine prefix can be removed. The
following commands can be used to create a clean wine prefix:

    # Create a seperate wine prefix and clean up an old wine prefix (when needed)
    export WINEPREFIX=/tmp/.wine_gcc_testsuite
    rm -rf $WINEPREFIX
    mkdir $WINEPREFIX

    # The command below will fail, but that's intentional
    # We only have to call a wine binary which triggers
    # the generation and population of a wine prefix
    winecfg || :

## Running the binutils testsuite

### Win32 target

Before performing these commands make sure a clean wine prefix is
created and the WINEPREFIX environment variable is set

If desired then parallel make can be used with 'make -j8' (where 8 is
number of parallel tasks which you want to run)

Perform these commands in the binutils source code folder:

    # Configure binutils in the build_win32 folder
    mkdir build_win32
    cd build_win32
    ../configure \
      --target=i686-w64-mingw32 \
      --disable-nls \
      --with-sysroot=/usr/i686-w64-mingw32/sys-root

    # Build binutils
    make

    # Run the testsuite
    make -k check

    # Collect testsuite results
    echo ====================TESTING WIN32 =========================
    cat {gas/testsuite/gas,ld/ld,binutils/binutils}.sum
    echo ====================TESTING WIN32 END======================

### Win64 target

Before performing these commands make sure a clean wine prefix is
created and the WINEPREFIX environment variable is set

If desired then parallel make can be used with 'make -j8' (where 8 is
number of parallel tasks which you want to run)

Perform these commands in the binutils source code folder:

    # Configure binutils in the build_win64 folder
    mkdir build_win64
    cd build_win64
    ../configure \
      --target=x86_64-w64-mingw32 \
      --disable-nls \
      --with-sysroot=/usr/x86_64-w64-mingw32/sys-root

    # Build binutils
    make

    # Run the testsuite
    make -k check

    # Collect testsuite results
    echo ====================TESTING WIN64 =========================
    cat {gas/testsuite/gas,ld/ld,binutils/binutils}.sum
    echo ====================TESTING WIN64 END======================

## Building and running the gcc testsuite

### Win32 target

Before performing these commands make sure a clean wine prefix is
created and the WINEPREFIX environment variable is set

If desired then parallel make can be used with 'make -j8' (where 8 is
number of parallel tasks which you want to run)

Perform these commands in the gcc source code folder:

    # Configure gcc in the build_win32 folder
    mkdir build_win32
    cd build_win32
    ../configure \
      --with-gnu-as --with-gnu-ld --verbose \
      --without-newlib \
      --disable-multilib \
      --disable-plugin \
      --with-system-zlib \
      --disable-nls --without-included-gettext \
      --disable-win32-registry \
      --enable-languages="c,c++,objc,obj-c++,fortran" \
      --with-ppl --with-cloog \
      --with-threads=posix \
      --enable-libgomp \
      --target=i686-w64-mingw32 \
      --with-sysroot=/usr/i686-w64-mingw32/sys-root

    # Build gcc
    make

    # Copy the GCC DLL's inside the wine prefix
    SYSTEM32_DIR=$WINEPREFIX/drive_c/windows/syswow64
    if [ ! -d $SYSTEM32_DIR ] ; then
        SYSTEM32_DIR=$WINEPREFIX/drive_c/windows/system32
    fi
    cp i686-w64-mingw32/libquadmath/.libs/libquadmath-0.dll $SYSTEM32_DIR
    cp i686-w64-mingw32/libgfortran/.libs/libgfortran-3.dll $SYSTEM32_DIR
    cp i686-w64-mingw32/libobjc/.libs/libobjc-4.dll $SYSTEM32_DIR
    cp i686-w64-mingw32/libssp/.libs/libssp-0.dll $SYSTEM32_DIR
    cp i686-w64-mingw32/libstdc++-v3/src/.libs/libstdc++-6.dll $SYSTEM32_DIR
    cp i686-w64-mingw32/libgcc/shlib/libgcc_s_sjlj-1.dll $SYSTEM32_DIR

    # When libgomp support is enabled
    cp i686-w64-mingw32/libgomp/.libs/libgomp-1.dll $SYSTEM32_DIR

    # When pthreads is used
    cp /usr/i686-w64-mingw32/sys-root/mingw/bin/pthreadGC2.dll $SYSTEM32_DIR

    # When winpthreads is used
    cp /usr/i686-w64-mingw32/sys-root/mingw/bin/libwinpthread-1.dll $SYSTEM32_DIR

    # According to Kai Tietz it's recommended to set the environment variable GCOV_PREFIX_STRIP
    export GCOV_PREFIX_STRIP=1000

    # Run the testsuite
    make -k check

    # Collect testsuite results
    echo ====================TESTING WIN32=========================
    ( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
    echo ====================TESTING WIN32 END=====================

### Win64

Before performing these commands make sure a clean wine prefix is
created and the WINEPREFIX environment variable is set

If desired then parallel make can be used with 'make -j8' (where 8 is
number of parallel tasks which you want to run)

Perform these commands in the gcc source code folder:

    # Configure gcc in the build_win64 folder
    mkdir build_win64
    cd build_win64
    ../configure \
      --with-gnu-as --with-gnu-ld --verbose \
      --without-newlib \
      --disable-multilib \
      --disable-plugin \
      --with-system-zlib \
      --disable-nls --without-included-gettext \
      --disable-win32-registry \
      --enable-languages="c,c++,objc,obj-c++,fortran" \
      --with-ppl --with-cloog \
      --with-threads=posix \
      --enable-libgomp \
      --target=x86_64-w64-mingw32 \
      --with-sysroot=/usr/x86_64-w64-mingw32/sys-root

    # Build gcc
    make

    SYSTEM64_DIR=$WINEPREFIX/drive_c/windows/system32
    cp x86_64-w64-mingw32/libquadmath/.libs/libquadmath-0.dll $SYSTEM64_DIR
    cp x86_64-w64-mingw32/libgfortran/.libs/libgfortran-3.dll $SYSTEM64_DIR
    cp x86_64-w64-mingw32/libobjc/.libs/libobjc-4.dll $SYSTEM64_DIR
    cp x86_64-w64-mingw32/libssp/.libs/libssp-0.dll $SYSTEM64_DIR
    cp x86_64-w64-mingw32/libstdc++-v3/src/.libs/libstdc++-6.dll $SYSTEM64_DIR
    cp x86_64-w64-mingw32/libgcc/shlib/libgcc_s_sjlj-1.dll $SYSTEM64_DIR

    # When libgomp support is enabled
    cp x86_64-w64-mingw32/libgomp/.libs/libgomp-1.dll $SYSTEM32_DIR

    # When pthreads is used
    cp /usr/x86_64-w64-mingw32/sys-root/mingw/bin/pthreadGC2.dll $SYSTEM32_DIR

    # When winpthreads is used
    cp /usr/x86_64-w64-mingw32/sys-root/mingw/bin/libwinpthread-1.dll $SYSTEM32_DIR

    # According to Kai Tietz it's recommended to set the environment variable GCOV_PREFIX_STRIP
    export GCOV_PREFIX_STRIP=1000

    # Run the testsuite
    make -k check

    # Collect testsuite results
    echo ====================TESTING WIN64=========================
    ( LC_ALL=C ../contrib/test_summary || : ) 2>&1 | sed -n '/^cat.*EOF/,/^EOF/{/^cat.*EOF/d;/^EOF/d;/^LAST_UPDATED:/d;p;}'
    echo ====================TESTING WIN64 END=====================
