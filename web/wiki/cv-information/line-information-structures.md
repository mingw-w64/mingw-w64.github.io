# CV Line Information Structures

## CV\_Line\_t

This structure has size of 16 bytes.

typedef struct CV\_Line\_t {  
uint32\_t offset;  
uint32\_t linenumStart;  
uint32\_t deltaLineEnd;  
uint32\_t fStatement;  
} CV\_Line\_t;

## CV\_Column\_t

This structure has size of 4 bytes.

typedef struct CV\_Column\_t {  
uint16\_t offColumnStart;  
uint16\_t offColumnEnd;  
} CV\_Column\_t;