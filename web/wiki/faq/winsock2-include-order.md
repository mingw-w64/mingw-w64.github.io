# winsock2.h include order

*Reason:*

windows.h includes winsock.h itself, therefore, if you include
winsock2.h after it, several redefinition conflicts arise.

*Solution:*

If you want to use the winsock2 api, you must include winsock2.h before
windows.h. Also make sure that no other headers include windows.h before
winsock2.h. On the other hand, if you want to use winsock 1.1 api,
similarly include winsock.h before windows.h to make sure that you have
the correct header. In fact, both winsock.h and winsock2.h include
windows.h themselves, therefore if you include either of them first, you
should not need including windows.h later.

Another solution is defining WIN32\_LEAN\_AND\_MEAN before including
windows.h (you can add -DWIN32\_LEAN\_AND\_MEAN to your CFLAGS, too),
and then including the skipped headers manually, such as winsock2.h (or
winsock.h).
