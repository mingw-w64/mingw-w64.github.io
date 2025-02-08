# gendef(1)

## NAME
gendef - DLL export extractor

## SYNOPSIS
**gendef** [*options*] <*DLL*>

## DESCRIPTION
**gendef** dumps DLL export information from 32- and 64-bit Windows executables (respectively PE32 and PE32+ executables).

## OPTIONS
- **-** - Dump to stdout
- **-h**, **--help** - Briefly describe the syntax and options
- **-a**, **--assume-stdcall** - Assume functions with ambiguous calling conventions use stdcall
- **-I**, **--include-def-path** *path* - Add additional search paths in which to look for hint .def files
- **-f**, **--no-forward-output** - Don't output forwarders

## OUTPUT
By default **gendef** writes the DLL export information to a file named after the DLL, replacing .dll with .def.

## KNOWN ISSUES
For 32-bit DLLs, **gendef** cannot detect if a function with no return value (void) exported by a DLL uses stdcall or cdecl. Two workarounds are available: either use the "*-a*" option to force stdcall calling conventions, or generate .def files for any DLLs the DLL you're interested in depends upon. **gendef** will read other .def files found in the working directory to determine the calling convention in use.

64-bit DLLs are not affected, since they only use a single calling convention.

## SEE ALSO
**genidl**(1)

## AUTHORS
**gendef** was written by Kai Tietz and Jonathan Yong of the MinGW-w64 project.

This manual page was written by Stephen Kitt <steve@sk2.org\>, based on information provided with the program and in the project's wiki, for the Debian GNU/Linux system (but may be used by others).