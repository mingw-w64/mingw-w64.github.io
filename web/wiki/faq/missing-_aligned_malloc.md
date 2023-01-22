# __mingw_aligned_malloc is missing!

For mingw-w64, use `_aligned_malloc` and `_aligned_free` instead.

## `_aligned_malloc` and friends are missing!

Due to workarounds to prevent definition clashing, you should include
headers in the following order for proper prototypes.

    #include <stdlib.h>
    #include <intrin.h>
    #include <malloc.h>
    #include <windows.h>
