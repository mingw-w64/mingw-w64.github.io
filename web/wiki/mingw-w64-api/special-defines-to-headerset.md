# Special defines to modify behaviour of header declarations

-   USE\_MINGW\_GNU\_SNPRINTF (Defines that vsnprintf & snprintf are
    using gnu-style format rules.)
-   USE\_MINGW\_SETJMP\_TWO\_ARGS (Defines that setjmp should use two
    arguments instead of one. By experiments it was found, that this
    method has an undocumented second argument pointing to current stack
    location. It is not know for which purpose this is used. For 64-bit
    mode the macro by default defined.)
