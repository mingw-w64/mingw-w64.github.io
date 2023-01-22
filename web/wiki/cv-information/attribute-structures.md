# CV Attribute Structures

## CV\_fldattr\_t

The structure CV\_fldattr\_t has a width of 16 bits.

typedef struct CV\_fldattr\_t {  
uint16\_t access : 2; / *see
[eCV\_access](./ecv_access.md)* /  
uint16\_t mprop : 3; / *see
[eCV\_methodprop](./ecv_methodprop.md)*
/  
uint16\_t pseudo : 1;  
uint16\_t noinherit : 1;  
uint16\_t noconstruct : 1;  
uint16\_t compgenx : 1;  
uint16\_t sealed : 1;  
uint16\_t unused : 6;  
} CV\_fldattr\_t;

## CV\_funcattr\_t

The structure CV\_funcattr\_t has a width of 8 bits.

typedef struct CV\_funcattr\_t {  
unsigned char cxxreturnudt : 1;  
unsigned char ctor : 1;  
unsigned char ctorvbase : 1;  
unsigned char unused : 5;  
} CV\_funcattr\_t;

## CV\_modifier\_t

The structure CV\_modifier\_t has a width of 16 bits.

typedef struct CV\_modifier\_t {  
uint16\_t isconst : 1;  
uint16\_t isvolatile : 1;  
uint16\_t isunaligned : 1;  
uint16\_t unused : 13;  
} CV\_modifier\_t;

## CV\_prop\_t

The structure CV\_prop\_t has a width of 16 bits.  
typedef struct CV\_prop\_t {  
uint16\_t packed : 1;  
uint16\_t ctor : 1;  
uint16\_t ovlops : 1;  
uint16\_t isnested : 1;  
uint16\_t cnested : 1;  
uint16\_t opassign : 1;  
uint16\_t opcast : 1;  
uint16\_t fwdref : 1;  
uint16\_t scoped : 1;  
uint16\_t hasuniquename : 1;  
uint16\_t sealed : 1;  
uint16\_t hfa : 2;  
uint16\_t intrinsic : 1;  
uint16\_t reserved : 2;  
} CV\_prop\_t;