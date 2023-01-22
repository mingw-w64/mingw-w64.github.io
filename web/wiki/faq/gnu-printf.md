# gnu printf

## Using Gnu style printf and scanf

On Windows, format specifiers like "%llu" will not work for 64bit
integers on XP or earlier. To mitigate this problem, use the `__mingw_*`
versions instead, for example:

    #include <stdio.h>

    int main(){
      __mingw_printf("%lld",0x8fffffffLL);
      return 0;
    }

Alternatively with the `__USE_MINGW_ANSI_STDIO` macro:

    #define __USE_MINGW_ANSI_STDIO 1
    #include <stdio.h>

    int main(){
      printf("%lld",0x8fffffffLL);
      return 0;
    }

## User printf and scanf

Code such as:

    #define __USE_MINGW_ANSI_STDIO 1
    #include <stdio.h>

    __attribute__((__format__ (printf, 2, 3))) int my_print(void *c, const char *s, ...){
      /* do something with c */
      return printf(s,arglist);
    }

still produce warning even if using gnu style formatting, since GCC will
assume printf MS style arguments on Windows. The workaround is to use
the `__MINGW_PRINTF_FORMAT` macro:

    #define __USE_MINGW_ANSI_STDIO 1
    #include <stdio.h>

    __attribute__((__format__ (__MINGW_PRINTF_FORMAT, 2, 3))) int my_print(void *c, const char *s, ...){
      /* do something with c */
      return printf(s,arglist);
    }

The `__MINGW_PRINTF_FORMAT` macro will be set to the proper attribute to
inform GCC of the correct format style.