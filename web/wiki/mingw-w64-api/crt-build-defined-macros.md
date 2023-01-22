# CRT's build defined macros

Any build related macro is prefixed by **BUILD\_** to indicates its
origin and kind.

The following macros for crt build are defined.

-   **BUILD\_CRT\_SHARED**

This macro controls the kind of library build. Tf the library should be
compiled as shared object (.dll) then this macro has to be defined with
value one. If the macro isn't defined or has its macro has value of
zero, then static version of library is build.

-   **BUILD\_CRT\_STARTUP**

This macro is defined, when the startup-code objects are build.

-   **BUILD\_MT**

This macro controls, if the library should be compiled thread-safe. This
option possible can be omitted completely, as even for static library
version thread-safety should be turned one.