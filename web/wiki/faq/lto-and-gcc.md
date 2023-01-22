# Link Time Optimization

## What is it?

Link time optimization allows GCC to perform optimizations at the
linking stage rather than the compile stage. It allows for some
optimization that are impractical to detect at compile time. As of
October 2009, the <a href="http://gcc.gnu.org/wiki/LinkTimeOptimization"
rel="nofollow">LTO</a> branch has been merged into the main GCC trunk
(4.5.0 trunk is in stage 3 as of writing). Early gcc 4.5 LTO uses the
ELF format for storing data, the final executable format can be
anything, including Windows PE. This is no longer the case with more
recent gcc versions, ELF is no longer used as an intermediate container.

## How do I use it?

While compiling individual translation units (individual .cpp or .c
files), just add -flto. For example, "g++ -o myclass.o -c myclass.cpp
-flto". Make sure to use "-flto" when linking too.

### Rebuild GCC

Make sure you are building at least GCC 4.6 or later. You can also use
--enable-lto to make it explicit. See
<a href="http://gcc.gnu.org/install/configure.html" rel="nofollow">this
link</a> for more GCC configure options.

## Problems

-   Q: I get \`cc1: error: unrecognized command line option "-flto"',
    what gives?
-   A: You need to rebuild gcc with libelf and --enable-lto, GCC 4.5.X
    onwards supports lto.
-   Q: Why does it take so long to compile something with -flto?
-   A: The code is compiled twice, once into relocatables, the next into
    LTO gimples, so this is expected.
-   Q: Why are my programs so large?
-   A: Use the following
    <a href="http://sourceware.org/ml/binutils/2009-11/msg00436.html"
    rel="nofollow">patch</a> if you are using a binutils older than
    2.20.51-20091125. The lto sections should be discarded after
    linking.
-   Q: My computer ran out of memory when linking. How do I avoid this?
-   A: Use "-fwhopr" instead of "-flto" when linking.