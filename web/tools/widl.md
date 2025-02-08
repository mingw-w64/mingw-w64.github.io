# widl(1)

## NAME
widl - Wine Interface Definition Language (IDL) compiler

## SYNOPSIS

**widl** [*options*] *IDL_file*

**widl** [*options*] --dlldata-only *name1* [*name2...*]

## DESCRIPTION

When no options are used the program will generate a header file, and possibly client and server stubs, proxy and dlldata files, a typelib, and a UUID file, depending on the contents of the IDL file. If any of the options `-c`, `-h`, `-p`, `-s`, `-t`, `-u` or `--local-stubs` is given, `widl` will only generate the requested files, and no others. When run with `--dlldata-only`, widl will only generate a dlldata file, and it will contain a list of the names passed as arguments. Usually the way this file is updated is that each time `widl` is run, it reads any existing dlldata file, and if necessary regenerates it with the same list of names, but with the present proxy file included.

When run without any arguments, `widl` will print a help message.

## OPTIONS

### General options:

- `-V` - Print version number and exit.
- `-o, --output=name` - Set the name of the output file. When generating multiple output files, this sets only the base name of the file; the respective output files are then named *name*.h, *name*_p.c, etc.
- `-b cpu-manufacturer[-kernel]-os` - Set the target architecture when cross-compiling. The target specification is in the standard autoconf format as returned by `config.sub`.

### Header options:

- `-h` - Generate header files. The default output filename is *infile*.h.
- `--oldnames` - Use old naming conventions.

### Type library options:

- `-t` - Generate a type library. The default output filename is *infile*.tlb. If the output file name ends in `.res`, a binary resource file containing the type library is generated instead.
- `-m32, -m64` - Generate a Win32 or Win64 type library respectively.

### UUID file options:

- `-u` - Generate a UUID file. The default output filename is *infile*_i.c.

### Proxy/stub generation options:

- `-c` - Generate a client stub file. The default output filename is *infile*_c.c.
- `-Os` - Generate inline stubs.
- `-Oi` - Generate old-style interpreted stubs.
- `-Oif, -Oic, -Oicf` - Generate new-style fully interpreted stubs.
- `-p` - Generate a proxy. The default output filename is *infile*_p.c.
- `--prefix-all=prefix` - Prefix to put on the name of both client and server stubs.
- `--prefix-client=prefix` - Prefix to put on the name of client stubs.
- `--prefix-server=prefix` - Prefix to put on the name of server stubs.
- `-s` - Generate a server stub file. The default output filename is *infile*_s.c.
- `--win32`, `--win64` - Only generate 32-bit or 64-bit code respectively (the default is to generate both 32-bit and 64-bit versions into the same destination file).
- `--rt` - Enable additional language extensions for IDL to support WinRT.

### Registration script options:

- `-r` - Generate a registration script. The default output filename is *infile*_r.rgs. If the output file name ends in `.res`, a binary resource file containing the script is generated instead.

### Dlldata file options:

- `--dlldata-only name1 [name2...]` - Regenerate the dlldata file from scratch using the specified proxy names. The default output filename is `dlldata.c`.

### Preprocessor options:

- `-I path` - Add a header search directory to path. Multiple search directories are allowed.
- `-D id[=val]` - Define preprocessor macro *id* with value *val*.
- `-E` - Preprocess only.
- `-N` - Do not preprocess input.

### Debug options:

- `-W` - Enable pedantic warnings.
- `-d n` - Set debug level to the non negative integer *n*. If prefixed with `0x`, it will be interpreted as a hexadecimal number. For the meaning of values, see the DEBUG section.

### Miscellaneous options:

- `-app_config` - Ignored, present for midl compatibility.
- `--local-stubs=file` - Generate empty stubs for call_as/local methods in an object interface and write them to *file*.

## DEBUG

Debug level *n* is a bitmask with the following meaning:
- 0x01 Tell which resource is parsed (verbose mode)
- 0x02 Dump internal structures
- 0x04 Create a parser trace (yydebug=1)
- 0x08 Preprocessor messages
- 0x10 Preprocessor lex messages
- 0x20 Preprocessor yacc trace

## BUGS

Bugs can be reported on the [Wine bug tracker](http://bugs.winehq.org).

## AUTHORS

`widl` was originally written by Ove Kåven. It has been improved by Rob Shearman, Dan Hipschman, and others. For a complete list, see the git commit logs. This man page was originally written by Hannu Valtonen and then updated by Dan Hipschman.

## AVAILABILITY

`widl` is part of the Wine distribution, which is available through WineHQ, the [Wine development headquarters](http://www.winehq.org/).

## SEE ALSO

[Wine documentation and support](http://www.winehq.org/help)