# The case against msvcrt.dll

Historically, Windows ports of gcc have used Microsoft's msvcrt.dll as
the only available C runtime. This is not necessarily a bad idea, as it
considerably simplifies deployment, and it gives gcc-compiled
application the classical UNIX guarantee that all code in a given
process shares the same version and instance of the C runtime library.
However, the use of msvcrt.dll in Windows ports of gcc (Cygwin first,
then MinGW) came with a large number of misconceptions. This article
will attempt to correct them. Possible ways out of this unfortunate
situation will be discussed in a future article.

## Myth \#1: msvcrt.dll is the latest version of the Microsoft C runtime

This was only true up to Visual Studio 6.0.

The idea at the time was that applications would install themselves
using the Setup API, which correctly handled shared DLLs by (among other
things) ensuring that an older version of a shared DLL would not
overwrite a newer version. All code compiled with the Microsoft
compilers would link to msvcrt.dll, which was installed globally (in the
system or system32 directory) and would always be the highest version
available.

This soon proved unrealistic, for two reasons:

-   the Microsoft C runtime would have to remain
    backwards-binary-compatible across major releases (name one C
    runtime that does);
-   application installers would more often than not overwrite the
    shared msvcrt.dll with an incompatible version.

The solution was twofold:

-   starting with Visual Studio .NET, the C runtime would have a
    versioned name (msvcr70.dll, msvcr71.dll, msvcr80.dll...);
-   starting with Windows 2000, msvcrt.dll would be made a system DLL
    and, as such, put under System File Protection, to prevent bad
    installers from overwriting it.

As a result, any current incarnation of msvcrt.dll is a hybrid between
the 6.0 runtime and the latest runtime at the time the respective
release of Windows was made. Binary compatibility with Visual Studio 6.0
and earlier is required by the fact that the new DLL "hijacked" the name
of the 6.0 runtime, so any version of the DLL is required to support all
applications compiled with Visual Studio 6.0. The hybridization with a
newer runtime is necessary because the 6.0 runtime is extremely old, and
a large number of API improvements have been made since its release.

**For all intents and purposes, msvcrt.dll is the 6.0 runtime**. All
bets are off regarding features introduced in later versions. They could
be supported, they could be not, they could be incompatible.

## Myth \#2: use of msvcrt.dll is fully supported by Microsoft

Outside of Visual Studio 6.0, msvcrt.dll is only supported in the
Windows DDK, whose build environment is almost the same build
environment used to build Windows itself. The msvcrt.dll import library
contained in the Windows DDK only links to 6.0 APIs. APIs introduced in
later versions of the runtime are included in the import library as
statically-linked implementations.

## Myth \#3: using &gt; 6.0 APIs from msvcrt.dll is safe and sound

By sheer coincidence, APIs introduced after 6.0 are almost
binary-compatible between msvcrt.dll and public runtime DLLs (such as
msvcr70.dll, msvcr71.dll...). Not only this cannot be relied upon, but
importing &gt; 6.0 APIs from msvcrt.dll has the rather undesireable
effect of tying an application to a specific version (or range of
versions) of Windows: if a public C runtime API first appeared in
Windows XP's msvcrt.dll, then an application that imports the API from
msvcrt.dll will not work on Windows 2000 or earlier versions.

Only Windows code itself is expected to use the full API exported by
msvcrt.dll. Regular applications are expected to limit themselves to the
6.0-safe subset.
