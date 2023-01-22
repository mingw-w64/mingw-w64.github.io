# testsuite status - gplusplus

## Summary

Number of expected passes 17608  
Number of unexpected failures 49  
Number of expected failures 82  
Number of unresolved testcases 43  
Number of unsupported tests 217

------------------------------------------------------------------------

## Failures

FAIL: g++.dg/bprob/g++-bprob-1.C execution: file g++-bprob-1.gcda does
not exist, -O0 -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-1.C execution: file g++-bprob-1.gcda does
not exist, -O1 -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-1.C execution: file g++-bprob-1.gcda does
not exist, -O2 -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-1.C execution: file g++-bprob-1.gcda does
not exist, -O3 -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-1.C execution: file g++-bprob-1.gcda does
not exist, -O3 -g -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-1.C execution: file g++-bprob-1.gcda does
not exist, -Os -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-2.C execution: file g++-bprob-2.gcda does
not exist, -g -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-2.C execution: file g++-bprob-2.gcda does
not exist, -O0 -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-2.C execution: file g++-bprob-2.gcda does
not exist, -O1 -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-2.C execution: file g++-bprob-2.gcda does
not exist, -O2 -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-2.C execution: file g++-bprob-2.gcda does
not exist, -O3 -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-2.C execution: file g++-bprob-2.gcda does
not exist, -O3 -g -fprofile-arcs  
FAIL: g++.dg/bprob/g++-bprob-2.C execution: file g++-bprob-2.gcda does
not exist, -Os -fprofile-arcs  
FAIL: g++.dg/abi/local1.C execution test  
FAIL: g++.dg/abi/offsetof.C (test for excess errors)  
FAIL: g++.dg/abi/rtti1.C scan-assembler-dem-not \\ntypeinfo for
A<a href="../%3A%20%02klzzwxh%3A0007%03%02klzzwxh%3A0008%03"
class="alink notfound">[: \t\n]</a>  
FAIL: g++.dg/abi/rtti3.C scan-assembler
.weak<a href="../%20%02klzzwxh%3A0009%03" class="alink notfound">[ \t]</a>*?\_ZTSPP1A  
FAIL: g++.dg/abi/thunk4.C scan-assembler
.weak<a href="../%20%02klzzwxh%3A0010%03" class="alink notfound">[ \t]</a>*?*ZThn.\_N7Derived3FooEv  
FAIL: g++.dg/eh/weak1.C execution test  
FAIL: g++.dg/ext/fnname3.C execution test  
FAIL: g++.dg/ext/utf-cvt.C (test for excess errors)  
FAIL: g++.dg/ext/utf16-4.C (test for warnings, line 16)  
FAIL: g++.dg/ext/utf16-4.C (test for excess errors)  
FAIL: g++.dg/ext/utf32-4.C (test for excess errors)  
FAIL: g++.dg/init/cleanup3.C scan-assembler-not \_tcf  
FAIL: g++.dg/init/struct1.C (test for excess errors)  
FAIL: g++.dg/init/struct2.C (test for excess errors)  
FAIL: g++.dg/init/struct3.C (test for excess errors)  
FAIL: g++.dg/other/large-size-array.C (test for errors, line 19)  
FAIL: g++.dg/other/large-size-array.C (test for errors, line 20)  
FAIL: g++.dg/other/pr25632.C (test for excess errors)  
FAIL: g++.dg/template/spec35.C scan-assembler
.weak(\_definition)?<a href="../%02klzzwxh%3A0011%03%20" class="alink notfound">[\t ]</a>\**?*Z2f2IiEvT*  
FAIL: g++.dg/tree-ssa/pr21082.C (test for excess errors)  
FAIL: g++.dg/tree-ssa/ssa-store-ccp-1.C scan-tree-dump-times optimized
"conststaticvariable" 1  
FAIL: g++.dg/torture/pr31579.C -O0 (test for excess errors)  
FAIL: g++.dg/torture/pr31579.C -O1 (test for excess errors)  
FAIL: g++.dg/torture/pr31579.C -O2 (test for excess errors)  
FAIL: g++.dg/torture/pr31579.C -O3 -fomit-frame-pointer (test for excess
errors)  
FAIL: g++.dg/torture/pr31579.C -O3 -g (test for excess errors)  
FAIL: g++.dg/torture/pr31579.C -Os (test for excess errors)  
FAIL: g++.dg/tree-prof/indir-call-prof.C execution: file
indir-call-prof.gcda does not exist, -g -fprofile-generate  
FAIL: g++.dg/tree-prof/indir-call-prof.C execution: file
indir-call-prof.gcda does not exist, -O0 -fprofile-generate  
FAIL: g++.dg/tree-prof/indir-call-prof.C execution: file
indir-call-prof.gcda does not exist, -O1 -fprofile-generate  
FAIL: g++.dg/tree-prof/indir-call-prof.C execution: file
indir-call-prof.gcda does not exist, -O2 -fprofile-generate  
FAIL: g++.dg/tree-prof/indir-call-prof.C execution: file
indir-call-prof.gcda does not exist, -O3 -fprofile-generate  
FAIL: g++.dg/tree-prof/indir-call-prof.C execution: file
indir-call-prof.gcda does not exist, -O3 -g -fprofile-generate  
FAIL: g++.dg/tree-prof/indir-call-prof.C execution: file
indir-call-prof.gcda does not exist, -Os -fprofile-generate  
FAIL: g++.old-deja/g++.brendan/array1.C (test for errors, line 6)  
FAIL: g++.old-deja/g++.jason/new3.C (test for excess errors)  
FAIL: g++.old-deja/g++.other/init18.C (test for excess errors)  
FAIL: g++.old-deja/g++.other/null1.C (test for excess errors)