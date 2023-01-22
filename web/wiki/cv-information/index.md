# CV Information

CV is an abbreviation of Code View. It is a debugging format used to
provide symbol (SYM) and type (TYPE) based information.

The base structure of TYPEs and SYMs has the following layout:

typedef struct CV\_TYPEDATA {  
uint16\_t blocksize;  
unsigned char
data<a href="../blocksize" class="alink notfound">[blocksize]</a>;  
} CV\_TYPEDATA;

typedef struct CV\_SYMDATA {  
uint16\_t blocksize;  
unsigned char
data<a href="../blocksize" class="alink notfound">[blocksize]</a>;  
} CV\_SYMDATA;

The field blocksize specifies the size of the following data.  
The CV\_TYPEDATA/CV\_SYM structure is aligned to 4 bytes. The blocksize
field includes this alignment. E.g. a CV\_TYPEDATA block with unaligned
content data (blocksize*) of 4 bytes has an aligned blocksize value of
6.  
The calculation rule is: blocksize = (((blocksize* + 2) + 3) & ~3) - 2;

Each data block begins with a leaf field, which specifies the kind of
the data block's data. SYMs and TYPEs have different sets of leaf (See
eCV\_symtags and eCV\_typtags).

## Enumerations

-   [eCV\_access](./ecv_access.md)
-   [eCV\_call](./ecv_call.md)
-   eCV\_HFA
-   eCV\_int
-   eCV\_integral
-   [eCV\_methodprop](./ecv_methodprop.md)
-   eCV\_pmtype
-   eCV\_prmode
-   eCV\_ptrmode
-   eCV\_ptrtype
-   eCV\_real
-   [eCV\_sourcechksum](./ecv_sourcechksum.md)
-   eCV\_special
-   eCV\_symtags
-   eCV\_type
-   eCV\_typtags

## Structures

-   [CV Attribute Structures](./attribute-structures.md)
-   [CV Line Information Structures](./line-information-structures.md)
