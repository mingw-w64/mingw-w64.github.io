# genidl(1)

## NAME
genidl - Windows typelib information extractor

## SYNOPSIS
**genidl** [*options*] <*file*>

## DESCRIPTION
**genidl** dumps IDL information found in typelib data present in 32- and 64-bit Windows executables and TLB files.

## OPTIONS
**-h**, **--help**
Briefly describe the syntax and options.

**-b** <*arg*>, **--basedumpname=**<*arg*>
Use *arg* as prefix of generated .idl files.

**-H**, **--header**
Generate a header.

**-d**, **--dump**
Dump additional debugging information.

**-v**, **--verbose**
Show additional status information.

## SEE ALSO
**gendef**(1)

## AUTHORS
**genidl** was written by Kai Tietz and Jonathan Yong of the MinGW-w64 project.

This manual page was written by Stephen Kitt <steve@sk2.org\> for the Debian GNU/Linux system (but may be used by others).
