# PPL and CLooG

PPL and CLooG are used by GCC for high level optimizations. As of August
2008, the new optimization method has been merged into GCC (4.4.0)
mainline, but maintains a separate branch known as
<a href="http://gcc.gnu.org/wiki/Graphite" rel="nofollow">Graphite</a>
for development.

# Enabling "Graphite" Enhancements

You'll need to install
<a href="http://www.cs.unipr.it/ppl/" rel="nofollow">PPL</a> (The Parma
Polyhedra Library, not to be confused with
<a href="http://icps.u-strasbg.fr/PolyLib/" rel="nofollow">PolyLib</a>)
and
<a href="http://repo.or.cz/w/cloog-ppl.git" rel="nofollow">CLooG/PPL</a>,
a port of CLooG to PPL.

## PPL and GMP

PPL depends on the C++ bindings for
<a href="http://gmplib.org/" rel="nofollow">GMP</a>, so GMP must be
built with --enable-cxx in configure. To allow C++ exception handling
thrown from PPL to propagate properly, make sure all GMP code is
compiled with CPPFLAGS="-fexceptions".

Note: For Windows based platform, GMP is either built as shared (DLL) or
static, but not both. It is preferable to build PPL and CLooG similarly
to how GMP was built.

## CLooG/PPL

Building CLooG is straight forward. For static builds, you should add
'--with-host-libstdcxx="-lstdc++ -lsupc++"' to the configuration script
to avoid link failures.

## Building GCC

When running the GCC configure script, remember to set --with-ppl and
--with-cloog to point to the PPL and CLooG install prefix. If you are
linking to static PPL and CLooG, add '--with-host-libstdcxx="-lstdc++
-lsupc++"' to prevent link failures when building the new GCC backends.
