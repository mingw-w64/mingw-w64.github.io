# search-paths-prefixes-and-relocation

## Prologue

All of the following is applicable to i686 mingw-w64 gcc builds, which
is compiled gcc-4.8.0 using rubenvb's personal i686-&gt;i686
(cross?)compiler, in MSys, using `--prefix=/mingw --with-sysroot=/root`,
where `/mingw` contains rubenvb's pre-built toolchain, while `/root` is
the place where gcc and its prerequisites are installed; once gcc is
compiled, mounts are changed - `/mingw` points to the place `/root` used
to point, and `/root` is removed completely, so that everything can be
configured with `--prefix=/mingw`, which is the usual convention. Most
of the code that the text below refers to is in `inpath.c`, `incpath.h`,
`cppdefault.c` and `cppdefault.h`.

## What happens

Most of the standard include paths, which are hard-coded into gcc, are
passed to the preprocessor via command line (there's a
`PREPROCESSOR_DEFINES` variable in Makefile), so they get DOSified (due
to MSYS path mangling) by the time they reach the code. At least two of
them are passed via `config.h` instead, and they don't get mangled.

"Get mangled" or "don't get mangled" does not map directly into "bad"
and "good" in this case (usually mangled paths in final binaries is
"bad"). Whether it is good or bad also depends on the `add_sysroot`
constant that is hard-coded for each path.

Gcc does the following with each hard-coded path:

    if add_sysroot==1 AND sysroot is not NULL:
      prepend sysroot to the path
    else if add_sysroot==0 AND path starts with a compile-time-prefix AND gcc was moved (determined at runtime):
      replace compile-time-prefix in the path with current gcc libexec prefix (determined at runtime)
    else:
      call update_path() on the path (on W32 update_path() mostly replaces '\\', '/' and little else).

In any case, the path is added to the list of include directories after
that.

Note that `sysroot` is `NULL` at run-time on W32 - it's initialized by
the `TARGET_SYSTEM_ROOT` macro, which is usually undefined; even if it
were to be defined, it would have to be an absolute DOSish path or an
absolute \*nixish path, and prepending it to anything wouldn't solve any
problem all by itself. One can pass `-isysroot` to set `sysroot` at
run-time, but that is only used in special cases.

The second branch, where path rewriting is done, is what works most of
the time on W32, and is the reason why gcc can be moved around and still
work. But it doesn't come into effect if `add_sysroot=1` for the path.
It also doesn't work if the path does not start with the configure-time
prefix (it is difficult to tell whether this is a real possibility or
not).

The third, `update_path()`, branch doesn't change anything on W32, as
stated above.

How these affect different hard-coded paths? Well, imagine that gcc is
configured with `--prefix=/mingw --with-sysroot=/root`, `/mingw` is
`c:/foo/bar/mingw`, `/root` is `c:/foo/bar/root`. In that case
`cpp_include_defaults` will contain the following:

    add_sysroot=0, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include/c++/4.8.0"
    add_sysroot=0, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include/c++/4.8.0/i686-w64-mingw32"
    add_sysroot=0, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include/c++/4.8.0/backward"
    add_sysroot=0, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/include"
    add_sysroot=1, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include"
    add_sysroot=1, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include"
    add_sysroot=0, "/root/include"
    add_sysroot=0, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/include-fixed"
    add_sysroot=0, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/../../../../i686-w64-mingw32/include"
    add_sysroot=1, "/mingw/include"
    add_sysroot=1, "/mingw/include"

Note that individual elements of that list are enabled and disabled via
preprocessor macros, so these paths could from from any pre-processor
variables, it's impossible to tell which ones. This list does not
include `c:/foo/bar/root` anywhere, and it is unknown at which
circumstances that might change.

The result (paths added to the search list), if gcc is moved into
`d:/zool` prefix after being built, is this:

    add_sysroot=0, "d:/zool/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include/c++/4.8.0"
    add_sysroot=0, "d:/zool/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include/c++/4.8.0/i686-w64-mingw32"
    add_sysroot=0, "d:/zool/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include/c++/4.8.0/backward"
    add_sysroot=0, "d:/zool/lib/gcc/i686-w64-mingw32/4.8.0/include"
    add_sysroot=1, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include"
    add_sysroot=1, "c:/foo/bar/mingw/lib/gcc/i686-w64-mingw32/4.8.0/../../../../include"
    add_sysroot=0, "/root/include"
    add_sysroot=0, "d:/zool/lib/gcc/i686-w64-mingw32/4.8.0/include-fixed"
    add_sysroot=0, "d:/zool/lib/gcc/i686-w64-mingw32/4.8.0/../../../../i686-w64-mingw32/include"
    add_sysroot=1, "/mingw/include"
    add_sysroot=1, "/mingw/include"

A keen eye might notice that none of these refer, in a DOSish form, to
`d:/zool/include`. The reason everything still works is that gcc also
has other sources of directories for this list, but they are added in
some other place. At least one of them is, apparently, the right one
(`d:/zool/include`).

Later on the paths that start with "/" (\*nixish paths) will be
interpreted by the OS as
`this directory, in the root of the drive on which current working directory is located`.
So, gcc will look for headers in `d:/mingw/include` and
`d:/root/include`. Or `f:/mingw/include` and `f:/root/include`. Depends
on what `CWD` is. This is the reason why for a long time now most mingw
suppliers strongly advised against having mingw in a root of a drive in
a `mingw` directory. For the build discussed here, `root` directory in a
root of current drive is also a don't-have-it-or-you'll-break-everything
kind of directory.

The paths that are DOSish absolute paths, but have `add_sysroot=1`, will
remain unchanged. So even though gcc is now in `d:/zool`, it will still
keep looking for include files in `c:/foo/bar/mingw/include`. I.e. gcc
will look in its "birth" directory.

## Fixing this

There are multiple factors at play, and any of them could, in theory, be
fixed in some way, affecting the overall result. But fixing only one of
them will, usually, not suffice.

For example, one might eliminate the effects of MSYS path mangling by
passing all path via `config.h` instead of using command line arguments.
That will make most (if not all) hard-coded paths be \*nix-ish, which is
not going to help, since current gcc code can do nothing with them on
W32. To fix them, gcc has to know how they are mapped, and that
information is not, and should not be, available to gcc at run-time.

Or one might force MSYS path mangling to affect all paths (pass
everything via commandline), thus potentially hard-coding only DOSish
paths. This sounds like a good solution, until you realize that
`/root/include` will be mangled into `c:/foo/bar/root`, but gcc will
compare paths to `c:/foo/bar/mingw` (which is its hard-coded
configure-time prefix), so these paths will be passed to the list
unchanged. So `/root/include` will turn from a
mingw-dir-in-the-root-of-a-drive kind of bug (well, technically,
root-dir-in-the-root-of-a-drive) into a gcc-includes-its-birth-directory
kind of bug. Unless gcc **also** remembers `c:/foo/bar/root` somewhere
(for whatever reason), or is made to remember it, and checks for it
being the beginning of the path, this solution would not fix everything.
It also doesn't fix existing gcc-includes-its-birth-directory bug caused
by a hard-coded DOSish path with `add_sysroot=1`.

Another possible fix is to check whether `add_sysroot` is really
necessary for some of the hard-coded paths and/or make that adjustable
at configure time. That will fix the `c:/foo/bar/mingw` birth-directory
bugs, but mingw-in-root-dir-of-a-drive bugs will remain. If mangling is
forced everything, a mangled version of `/root/include` will still pose
a problem, that can only be fixed by making gcc also check for
`c:/foo/bar/root` alongside `c:/foo/bar/mingw` (see above).

A very invasive (but very effective) fix is to change the way gcc
remembers these paths. Make it split the path, at configure time, into a
prefix part and a path part, so gcc will remember `/mingw` and
`/include` separately. Then it can replace `/mingw` with current prefix
at run-time. That's how most projects deal with that kind of issues.

A small fix: make gcc throw away all \*nixish paths on W32 (since we
know pretty well that using these on W32 cannot, in any circumstances,
lead to anything meaningful). That will remove all
mingw-dir-in-the-root-of-a-drive bugs. The birth-directory bug will
remain. What's good about this fix is that it's easy to make, and it's
very straightforward (unlikely to have any unforeseen consequences) -
that is, as long as throwing-away part is kept to the
`add_standard_paths` function.

## What worked

Here is one way of sidestepping the issue:

-   Cross-compile gcc from a GNU system (thus eliminating the mangling
    problem). Cross-compiling from Cygwin might also work.
-   Configure with `--prefix=/mingw` . Since `/mingw` is not a valid
    directory on the build machine, a `--with-native-system-header-dir`
    pointing at the cross-compiler's target header directory (i.e.
    `/foo/bar/cross-compiler/i686-w64-mingw32/include`) is needed
-   Do the small fix outlined above - make gcc throw away, at runtime,
    any include directories that, after processing, still begin with
    `/`, since they are not usable.

That way:

-   Birth directory bug does not appear (thankfully)
-   mingw-dir-in-the-root-of-a-drive bug does not appear (thanks to the
    fix)
-   gcc does look in `${runtime_prefix}/include` and
    `${runtime_prefix}/lib` (that is, behaves like a native gcc - as
    intended)