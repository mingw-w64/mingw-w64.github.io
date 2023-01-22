# CV Enumerator eCV_call

This enumerator specifies the calling convention used.

typedef enum eCV\_call {  
CV\_CALL\_NEAR\_C = 0,  
CV\_CALL\_FAR\_C = 1,  
CV\_CALL\_NEAR\_PASCAL = 2,  
CV\_CALL\_FAR\_PASCAL = 3,  
CV\_CALL\_NEAR\_FAST = 4,  
CV\_CALL\_FAR\_FAST = 5,  
CV\_CALL\_SKIPPED = 6,  
CV\_CALL\_NEAR\_STD = 7,  
CV\_CALL\_FAR\_STD = 8,  
CV\_CALL\_NEAR\_SYS = 9,  
CV\_CALL\_FAR\_SYS = 10,  
CV\_CALL\_THISCALL = 11,  
CV\_CALL\_MIPSCALL = 12,  
CV\_CALL\_GENERIC = 13,  
CV\_CALL\_ALPHACALL = 14,  
CV\_CALL\_PPCCALL = 15,  
CV\_CALL\_SHCALL = 16,  
CV\_CALL\_ARMCALL = 17,  
CV\_CALL\_AM33CALL = 18,  
CV\_CALL\_TRICALL = 19,  
CV\_CALL\_SH5CALL = 20,  
CV\_CALL\_M32RCALL = 21,  
CV\_CALL\_CLRCALL = 22,  
CV\_CALL\_RESERVED = 23  
} eCV\_call;