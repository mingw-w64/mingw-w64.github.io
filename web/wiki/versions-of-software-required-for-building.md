# Versions of software required for building

Mingw-w64 can be a fast-moving target. This page provides a list of
software versions you can use together when building.

# Latest set of versions known to be working together

#### Mandatory components

Component  
Version at least  
Version at most  
Comment

GCC  
4.6.0  
HEAD

Binutils  
2.20.51  
HEAD

Mingw-w64 CRT  
HEAD

GMP  
4.3.2  
HEAD

MPFR  
2.4.1  
HEAD

MPC  
0.8.2  
HEAD

#### Only required for PPL (more optimizations)

Component  
Version at least  
Version at most  
Comment

PPL  
0.11  
HEAD

ClooG-PPL  
0.15.10  
HEAD  
must be ppl

#### Others (version requirements don't change often)

Component  
Version at least  
Version at most  
Comment

Bison  
any  
HEAD

Flex  
any  
HEAD

Coreutils  
HEAD

Make  
3.81  
HEAD

Perl  
any  
HEAD  
optional: for pod2man

gperf  
HEAD  
optional: for developping on gcc
