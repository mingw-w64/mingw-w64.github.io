# Contribute

!!! warning
    The information on this page is outdated and needs to be updated.

Mingw-w64 and the ecosystem surrounding it are stable and with many features.
There are however some topics for which developer-time has been scarce. This
page lists tasks that are relatively simple and can be worked on without the
need for a huge background while still being important and high on the
wish-lists of users.

In order to avoid duplicate efforts, if you take on one of these tasks, please
mention it on the
[mailing-list](https://lists.sourceforge.net/mailman/listinfo/mingw-w64-public).

The tasks below have been split enough to be simple and fairly well-contained
while still being useful on their own. Most could be internship topics.

There are references to other websites on this page; their presence does not
constitute an endorsement in any way.

## Win32 API and Runtime

Mingw-w64 is constantly looking for updates to its win32 API headers from [MSDN
Library](https://msdn.microsoft.com/en-us/library/). If you believe you have
found an API that is not available in mingw-w64 but is documented as part of
MSDN or a mistake in mingw-w64, please do not hesitate to contact us through the
[mailing-list](https://lists.sourceforge.net/mailman/listinfo/mingw-w64-public).

For patch submissions, please remember to use sign-off your git commits before
submitting the patches to the
[mailing-list](https://lists.sourceforge.net/mailman/listinfo/mingw-w64-public).
Both git send-email and git format-patch forms are allowed. From past
experiences however, if you do use an email client to attach individual patches,
please use the .txt extension, especially for Google Mail users so the patch
does not get treated as a binary.

## SEH for 32bits

The patent for SEH for 32bits has now expired and while new computers
are all 64 bits, Intel has continued selling Atom CPUs that only handled
32 bits very late and some applications are still 32 bits. Projects such
as Wine and ReactOS will also benefit from 32bits SEH. Overall the need
is still there and will continue for years to come and will outlast
Microsoft's support for 32bits.

Note that you will need FSF paperwork since the work has to be done
inside GCC. Check CC's page on contributing.

- [The now-expired patent on SEH](https://www.google.com/patents/US5628016)
- [A Crash Course on the Depths of Win32™ Structured Exception Handling](https://www.microsoft.com/msj/0197/exception/exception.aspx)
- [Win32 Exceptions – OS Level Point of View](https://www.codeproject.com/Articles/82701/Win-Exceptions-OS-Level-Point-of-View)
- [How a C++ compiler implements exception handling](https://www.codeproject.com/Articles/2126/How-a-C-compiler-implements-exception-handling)
- [Structured Exception Handling Basics](https://www.gamedev.net/page/resources/_/technical/general-programming/structured-exception-handling-basics-r1272)
- [Windows' SEH and C++ Exception Handling](https://www.gamedev.net/page/resources/_/technical/general-programming/windows-seh-and-c-exception-handling-r1291)
- [Structured Exception Handling Considered Harmful](http://blogs.msdn.com/b/larryosterman/archive/2004/09/10/228068.aspx)
- [SEH and C++ Exceptions - catch all in one](https://www.codeproject.com/Articles/422/SEH-and-C-Exceptions-catch-all-in-one)
- [GCC sources](https://gcc.gnu.org/git/?p=gcc.git) and
  [unwind-seh.c](https://gcc.gnu.org/git/?p=gcc.git;a=blob;f=libgcc/unwind-seh.c;hb=HEAD)
  in particular. Note that 32-bit SEH is stack-based and requires
  code-generation unlike 64bits SEH which is simply table-based (that difference
  explains why the patent only mattered to 32bits).

## Sanitizers (ASAN, TSAN, USAN)

Sanitizers are runtime checks for a number of situations which have
usually required instrumentation with tools that cause an important
slowdown (like Valgrind).

They are relatively new and much lighter than other approaches.

### Thorough Status Report for Sanitizers (asan, tsan, usan)

ASAN, TSAN and USAN are great technologies which are available in GCC.
Unfortunately they are not completely usable on Windows. A proper review
and tests are needed before anything.

### Fixing remaining bits in asan, tsan or usan (see above)

Once a report on the status is available, work on it can be started.

## Link-Time Optimization (LTO)

Optimizations in C cannot cross compilation units and many of them are
therefore missed in large applications and when using libraries. LTO
runs some optimizations during linking, when the toolchain can see all
the objects at once and run cross-unit optimizations.

### Thorough Status Report for LTO

LTO has recently been improved a lot in GCC and binutils. There are
still some issues on Windows though. The first step to making it work is
to get a proper and up-to-date test and to identify the
platform-specific bugs.

### Fixing remaining bits in LTO

Fix the issues found by the status report from above. The actual bug
list will be updated as it becomes available.

## Compiler plugin for Visual Studio

A compiler plugin would make GCC, binutils tools and GDB available from
the Visual Studio IDE. Most people state they stick with VS because of
the IDE; such a plugin would allow mixing the two.

[VisualGDB](http://www.visualgdb.com/) (commercial) provides such a plugin,
apparently meant for compiling to micro-controllers and Linux (Android or not).

## Debug Infos

PDB is the file-format used by Microsoft to store debug info.
Unfortunately it is undocumented.

### Documentation of the PDB file-format

Since the format is undocumented, first step is to document it.
Fortunately, during the past few years, reader and possibly writer code
has appeared, mostly out of Microsoft.

- A [library named ''dump_syms''](https://github.com/luser/dump_syms.git) is
  available. It can read PDB files at least to some extent. Licensing and origin
  need to be checked.

- Microsoft has released [Roslyn, a ".NET Compiler
  Platform"](http://roslyn.codeplex.com/). It contains a [PDB writer
  implementation](https://roslyn.codeplex.com/SourceControl/latest#Src/Compilers/Core/Portable/PEWriter/PdbWriter.cs).
  This may be an actual implementation or only an interface to the actual one.
  It is difficult to say without further analysis.

- Microsoft has also released [CCI Metadata](http://ccimetadata.codeplex.com/)
  under the [MS-PL](https://opensource.org/licenses/ms-pl.html). It contains [PDB
  reader
  implementation](http://ccimetadata.codeplex.com/SourceControl/latest#Sources/PdbReader/)
  that should constitute an appropriate source.

### Creation of PDB files

Creating PDB files will allow the Microsoft tools to make meaningful
backtraces when code built with free compilers is involved.

### Handling of PDB in GDB

Reading PDB files will allow free tools to make meaningful backtraces
when code built with MSVC is involved.

### Translation from/to PDB

Most often debug information will only be available in a single format. Being
able to convert between them when needed will be useful.

## C11 and C++11 Threading Support

### C11 Threading and Atomics

The C11 standard has a section on threading which is still left unimplemented on
several platforms. The API follows pthreads' quite closely and it is left to the
implementer to decide whether to base it on winpthreads or directly on the (>=
Vista) Win32 API.

[The final C11 draft](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf)
is identical to the standard but is available freely.

Note that you will need FSF paperwork since the work has to be done inside GCC.
Check [GCC's page on contributing](https://gcc.gnu.org/contribute.html).

### Implementation of C11 and C++11 Threading Support Without Winpthreads

#### mcfgthread

The [mcfgthread](https://github.com/lhmouse/mcfgthread) library aims at
providing an efficient implementation of thread support for GCC that is required
by the C11 and C++11 standard. It uses a lot of undocumented Windows NT syscalls
to ensure performance. Its introduction and manual can be found from its [wiki
pages](https://github.com/lhmouse/mcfgthread/wiki).
