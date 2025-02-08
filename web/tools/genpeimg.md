# genpeimg(1)

## NAME
genpeimg - Modify Portable Executable flags and properties

## SYNOPSIS
**genpeimg** [*options*] *files*...

## DESCRIPTION
genpeimg is a tool for modifying characteristics and properties of Portable Executable (PE) files. It can modify PE header characteristics, DLL characteristics, and the subsystem type.

## OPTIONS

**-p [+|-]flags**
Modify PE header characteristics. Flags can be prefixed with + to set or - to clear:

- `l` - Large address aware (32-bit only)
- `r` - Removable run from swap
- `n` - New run from swap
- `s` - System
- `u` - Up system only

**-d [+|-]flags**
Modify DLL characteristics. Flags can be prefixed with + to set or - to clear:

- `e` - High entropy VA
- `d` - Dynamic base
- `f` - Force integrity
- `n` - NX compatible
- `i` - No isolation
- `s` - No SEH
- `b` - No bind
- `a` - App container
- `w` - WDM driver
- `c` - Control flow guard
- `t` - Terminal server aware

**-s subsystem**
Set the PE subsystem. Valid values are:

- BOOT_APPLICATION
- CONSOLE
- EFI_APPLICATION
- EFI_BOOT_SERVICE_DRIVER
- EFI_ROM
- EFI_RUNTIME_DRIVER
- NATIVE
- POSIX
- WINDOWS
- OS2
- NATIVE_WINDOWS9X
- WINDOWS_CE
- XBOX
- UNKNOWN

Or a numeric value.

**-x**
Dump PE image information to stdout

**-h**
Show help information

## AUTHORS

This manual page was written by Christoph Reiter <reiter.christoph@gmail.com\>.