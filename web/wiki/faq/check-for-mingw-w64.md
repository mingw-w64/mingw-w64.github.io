# Check for mingw-w64 headers

For checking if you are using mingw-w64 header-set and runtime you can
use the following piece of code for:

      #ifdef __MINGW32__
      # include <_mingw.h>
      # ifdef __MINGW64_VERSION_MAJOR
         /* This is a mingw-w64 header-set.  */
      # else
         /* This is a mingw.org header-set.  */
      # endif
      #else
        /* This is no gcc based runtime.  */
      #endif

Additionally on configure-stage you can check for existance of the
function mingw\_get\_crt\_info in libmingwex.a library.

      const char *__mingw_get_crt_info (void);
