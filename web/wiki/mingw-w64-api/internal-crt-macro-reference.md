# Internal CRT macro reference

Any internal macro of library is prefixed by two underscores.

-   **\_ CRTEXPORT**

This macro gets defined in w64crt\_defs.h file dependent to the build
specified macros **BUILD\_CRT\_SHARED** and **BUILD\_CRT\_STARTUP**. It
is used for the import/export semantic of functions and variables.
