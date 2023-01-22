# devel crt licensing, Coding-style, and more

### General information about ironCrate

The goal of ironCrate is to provide a full MS compatible C-runtime
library usable for user-mode and kernel-mode. It shall be compilable by
gcc and VC.

The ironCrate project uses BSD license.

-   What kind of file header do we use? The full license text is pretty
    long, therefore I'm against putting it into every file. Instead I
    suggest a small header with the project name name, pointing to the
    licence (see LICENSE.BSD file) + (c) ironCrate developer team or
    something like that.
-   Agreed. I've added LICENSE text file in top-level. Please take a
    look. IMHO we should use here term "(c) ironCrate developer team"
    plus "see AUTHORS file for list of individuals."

The coding style needs to be defined in more detail. The following rules
are already defined so far:

-   No C++ comments in source
-   No author remarks in source and headers. Please use here instead the
    AUTHORS file in top-level directory.
-   If inline assembler is necessary, separate those functions into
    compiler/target specific files. As VC doesn't have the ability to
    use inline-assembler within C for x64 target, the assembly-routines
    for this target need to be written in separate assembly files.
-   For optimizing C code via assembler a generic pure C version has to
    be provided, too.
-   We use cmake as make-system.
-   User-mode runtime will be provided as static and as shared variant.
-   Kernel-mode runtime will be provided only as static variant.
-   We don't use version conditional build for base-library. Instead
    each version specific implementation has an unique internal name. We
    don't use conditional \#if-guards to separate between different
    runtime-versions. Instead we are using mapping files to provide
    final exported and user-seen symbol-names.
-   Each variable and function in ironCrate has an internal name. \*\*
    This can get ugly, as we would use internal names when calling the
    functions, too. Also its harder to find the functions in code
    documentation (like doxygen). --tkreuzer 14:53, 27 March 2011 (UTC)
-   The ironCrate library uses its own internal header-set for
    C-runtime. We don't use here the global user-headers for C-runtime.
    \*\* I suggest seperating public and internal definitions, so that
    it could still be compiled with other public headers.
-   Before any new implementation gets accepted, testcases and
    online-documentation shall be present and approved.
-   For patches and discussions mingw-w64-ironCrate mailing-list shall
    be used.

Suggested coding styles:

-   Use portable assembler like used in reactos, which is compilable on
    both GAS and ML/ML64, Other assemblers could probably be supported
    as well. Its being preprocessed with CPP and in intel syntax.
    --tkreuzer 14:53, 27 March 2011 (UTC)
-   Use Allman or 1TBS indentation style. I heavily oppose GNU style.
    --tkreuzer 14:53, 27 March 2011 (UTC)
