# Notable Configure Options

This page list notable options when building mingw-w64 from source

## Headers

```
--enable-secure-api - Allows the use of *_s by default
--with-default-win32-winnt - sets the default _WINT32_WINNT value, defaults to 0x502. Do not change if you do not understand the implications.
--enable-sdk=ARG - Option to install DirectX SDK (directx) and Device Driver SDK (ddk).
```

## CRT

```
--enable-experimental - Enable 128-bit and decimal float printf
```