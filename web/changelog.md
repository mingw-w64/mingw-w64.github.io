# Changelog

## v10.0.0: [2022-04-04](https://sourceforge.net/p/mingw-w64/mailman/message/37635065/)

Notable changes:

- New msvcrt10, 20, 40, 70 and 71 import libraries.
- Drop x86_64 64bit crtdll.dll
- Updated wine imports
- Fix intrin.h compatibility with GCC-11
- `_(v)scprintf` optimization
- optimize `__ms_vsnprintf` for LTO

And many other additions thanks to, but not limited to (in Alphabetical
order)

Biswapriyo Nath, Corinna Vinschen, davjam, Jacek Caban, Jeremy Drake, Jonathan
Marler, Liu Hao, Mark Harmstone, Martin Storsjö, Matheus Izvekov, Michel Zou,
Ozkan Sezer, Pali Rohár, Patrick Northon, Ruslan Garipov, Steve Lhomme, Tom
Ritter

## v9.0.0: [2021-05-22](https://sourceforge.net/p/mingw-w64/mailman/message/37287751/)

Notable changes:

- UCRT updates by Biswapriyo Nath
- Wine updates by Jacek Caban
- Various new and updated API headers by Biswapriyo Nath and Liu Hao
- Various UCRT and MSVCRT fixes by Martin Storsjö
- `at_quick_exit` implementation by Martin Storsjö
- dism API by Biswapriyo Nath
- idl fixes by Steve Lhomme
- Winpthreads fixes by Liu Hao
- gettimeofday precision increase by Christian Franke

And many other additions thanks to, but not limited to (in Alphabetical order)

Alex Henrie, Andrew Eikum, Biswapriyo Nath, Christian Franke, Christoph
Reiter, DAVID MAY, Jacek Caban, Jeremy Drake, Jonathan Yong, Liu Hao, Mark
Harmstone, Martin Storsjö, Mateusz Mikuła, Nikolay Sivov, Ozkan Sezer, Pierre
Lamot, Rafał Harabień, Scr3amer, Steve Lhomme

## v8.0.0: [2020-09-18](https://sourceforge.net/p/mingw-w64/mailman/message/37111166/)

Notable changes:

- New Hyper-V headers and libraries by Biswapriyo Nath
- Many headers updated from Wine by Jacek Caban.
- ARM math improvements by Martin Storsjö
- floating point fixes by Liu Hao
- many `*printf` compatibility fixes by Liu Hao and Martin Storsjö
- massive Windows App Store API updates by Steve Lhomme
- winstorecompat library updates by Martin Storsjö
- `USE_MINGW_ANSI_STDIO` now automatically enabled in C99 and C11mode when not using UCRT by Pali Rohár
- wdm and ddk updates by Zebediah Figura
- UCRT for Windows Store Apps (-lucrtapp) by Martin Storsjö
- Audioclient and ActivateAudioInterfaceAsync API updates by Liu Hao
- DirectX SDKs are now always installed

And many other additions thanks to, but not limited to (in Alphabetical order)

Alex Henrie, Biswapriyo Nath, Eric Hassold, Jacek Caban, Jehan Pagès, Kleis Auke
Wolthuizen, Liu Hao, Martin Mitáš, Martin Storsjö, Nikolay Sivov, Noah Treuhaft,
Pali Rohár, Ruslan Garipov, Sanketh Menda, sezero, Stephan Ruloff, Stephen Kitt,
Steve Lhomme, Tom Ritter, xtne6f, Zebediah Figura, 屈佳伟

## v7.0.0: [2019-11-10](https://sourceforge.net/p/mingw-w64/mailman/message/36804945/)

Notable changes:

- `_FORTIFY_SOURCE` support thanks to Christian Franke.
- Lots of math fixes from Martin Storsjö.
- Many headers updated from Wine by Jacek Caban.
- UCRT support by Martin Storsjö.

And many other additions thanks to, but not limited to (in Alphabetical
order)

Alexey Pavlov, Antoine Cœur, Biswapriyo Nath, Chris Charabaruk, Christian
Franke, Hugo Beauzée-Luyssen, Jacek Caban, James Ross-Gowan, Johannes Pfau, Kai
Tietz, Liu Hao, Marisa-Chan, Martin Storsjö, Marvin Scholz, Mateusz Brzostek,
Matthew Palermo, Nikolay Sivov, Pierre Lamot, Richard Pospesel, Ruslan Garipov,
sezero, SquallATF, Steve Lhomme, Tomáš Golembiovský, Tom Ritter, xnor, Zach
Bacon, Zebediah Figura, Руслан Ижбулатов

## v6.0.0: [2018-09-17](https://sourceforge.net/p/mingw-w64/mailman/message/36416777/)

Notable changes:

- C++ `__cxa_atexit` thanks to Martin Storsjö and Liu Hao
- Massive additions to support UCRT thanks to Martin Storsjö
- Sync COM interface headers with Wine development thanks to Jacek Caban
- WinRT additions thanks to Hugo Beauzée-Luyssen
- ARM32 and ARM64 additions thanks to Martin Storsjö
- CRT library api-ms-win-core additions thanks to Martin Storsjö
- CRT library def file reorganization thanks to Martin Storsjö

And many other additions thanks to, but not limited to (in Alphabetical
order)

Alexey Pavlov Alon Bar-Lev André Hentschel Arthur Edelstein Corinna
Vinschen David Grayson David Wohlferd Ebrahim Byagowi Guy Helmer Hugo
Beauzée-Luyssen Ihsan Akmal Jacek Caban James Ross-Gowan Jean-Baptiste
Kempf Jonathan Yong Jon Turney Kai Tietz Liu Hao Martell Malone Martin
Storsjö Mateusz Matheus Izvekov mati865 Michał Janiszewski Nikolay Sivov
niXman Petri Hodju Ray Donnelly Ruben Van Boxem Ruslan Garipov Samuel D.
Leslie sezero Soar Qin Tamar Christina Tamir Duberstein Tim Hutt Tom
Ritter Yuta Nakai Алексей Павлов Руслан Ижбулатов 宋冬生

## v5.0.4: [2018-06-04](https://sourceforge.net/p/mingw-w64/mailman/message/36333746/)

- Fix gcc-8.1.0 compatibility regarding _xgetbv
- `%e` printf specifier will now produce at least 2 digits for the
  exponent.

## v5.0.3: [2017-11-04](https://sourceforge.net/p/mingw-w64/mailman/message/36103143/)

- pseudo-reloc will now try to restore page protection settings prior
  to manipulating it, rather than simply assuming it was read-only
  with execute.
- winpthreads: Fix undefined `__divmoddi4` when compiling with newly
  bootstrapped gcc-7
- Fixed modf family segfault due to eax clobbering.

## v5.0.2: [2017-03-28](https://sourceforge.net/p/mingw-w64/mailman/message/35754067/)

- RegSetKeyValueW now has proper wide arguments.
- Fix some crashes in winpthreads due to misaligned memory access when
  used with some SSE instructions.
- Fix pdh.h function calls to have proper stdcall decorators.

## v5.0.1: [2017-01-06](https://sourceforge.net/p/mingw-w64/mailman/message/35588585/)

- Don't use feature `(__attribute__((gcc_struct)))` that isn't supported on
  clang when compiling on clang thanks to David Wohlferd.
- Various ARM math fixes thanks to Martin Storsjö
- Removed some duplicate uuids defintions, thanks to HugoBeauzée-Luyssen.
- Define `IN6_IS_ADDR_` macros to conform to Posix Specm thanks toJean-Baptiste
  Kempf
- dxva.h: Add support for VP8/9 in DxVA2 thanks to Yuta Nakai

## v5.0.0: [2016-10-19](https://sourceforge.net/p/mingw-w64/mailman/message/35437019/)

- Fixes to the `__mingw_printf` family of functions.
- DirectX updates from Wine.
- Various updates to support Windows 7 and 10.
- Various header typo fixes.

## v4

- 32bit ARM thumb software math (Thanks to André Hentschel!).
- New ftw() support for gcc-5.x support.
- Experimental printf changes - Ability to print 128bit integers
  (%I128\*) and Decimal Floats (%H, %D), disabled by default. Build
  the CRT with `--enable-experimental` to use.
- Updated OpenGL 4.5 headers.
- Better DirectX 11 support.
- Better Windows 7, 8/8.1 API support.

## v3

- Required for GCC 4.8.
- Much improved floating point math performance.
- Improved MSVC intrinsics performance.
- Addition of wide variants in C99 printf and scanf.
- Partial C1X secure CRT support.
- Partial MS Secure CRT templates for C++.
- Vastly improved Windows 7 and 8 win32 API support.
- POSIX-style Large File Support.
- Winpthread: new library, pthreads implementation for Windows.
- Winstorecompat: new library for Windows Store compatibility (WIP).

## v2

- Expanded Windows Vista/7 API support.
