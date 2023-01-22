# Why doesn't mingw-w64 gcc support Dwarf-2 Exception Handling?

The Dwarf-2 EH implementation for Windows is not designed at all to work
under 64-bit Windows applications. In win32 mode, the exception unwind
handler cannot propagate through non-dw2 aware code, this means that any
exception going through any non-dw2 aware "foreign frames" code will
fail, including Windows system DLLs and DLLs built with Visual Studio.
Dwarf-2 unwinding code in gcc inspects the x86 unwinding assembly and is
unable to proceed without other dwarf-2 unwind information.

The SetJump? LongJump? method of exception handling works for most cases
on both win32 and win64, except for general protection faults.
Structured exception handling support in gcc is being developed to
overcome the weaknesses of dw2 and sjlj. On win64, the
unwind-information are placed in xdata-section and there is the .pdata
(function descriptor table) instead of the stack. For win32, the chain
of handlers are on stack and need to be saved/restored by real executed
code.
