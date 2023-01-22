# Thread Local Storage (TLS) and Fiber Local Storage (FLS)

The C-runtime needs to keep various variables in TLS/FLS memory, so that
those values get for each thread separated. This feature is a
requirement for support thread-safe multi-threaded applications.

Some C-runtime variables have to be stored in TLS/FLS storage for each
thread.

External seen variable are:

-   errno
-   doserrno

Internal used variables for standard C functions are

-   asctime()'s return buffer string (ASCII)
-   ecvt()'s and fcvt()'s internal string buffer
-   gmtime()'s return structure
-   mbstol()'s last found token (Mulibyte-Character)
-   putch()'s buffer for multibyte/ascii internal buffer and flag value
-   rands()'s last random number range.
-   strerror()'s return buffer string (ASCII)
-   strtok()'s last found token (ASCII)
-   tmpnam()'s return buffer string (ASCII)
-   wasctime()'s return buffer string (Wide-Character)
-   wcserror()'s return buffer string (Wide-Character)
-   wcstok()'s last found token (Wide-Character)
-   wtmpnam()'s return buffer string (Wide-Character)

Additional internal used variables for threading, exception handling,
and internal managment are:

-   Architecture dependent data
-   Base information for the thread itself (its id, handle)
-   Data for beginthread information
-   Data for exception handling
-   Data for locale information
-   Data for multibyte character information
-   Data for signal handling

For x86 there are two ways for implementing thread local storage. The
standard is by using the Tls&lt;...&gt; API, for newer 32-bit OSes
(Windows Vista, Windows 2008) Fls&lt;...&gt; API is used instead. It is
dependents on the existance of the Fls&lt;...&gt; API in Kernel32.dll
library.  
For x64 Windows OSes, there is always Fls&lt;...&gt; API present. As far
as we found out is just the Fls&lt;...&gt; API used for this targets in
msvcrt.dll and no Tls&lt;...&gt; is used here.