#ifndef TYPE_NAME_H
#define TYPE_NAME_H

#define TYPE_NAME(x) _Generic((x), \
    _Bool: "_BOOL", \
    char: "char", \
    signed char: "signed char", \
    unsigned char: "unsigned char", \
    short: "short", \
    unsigned short: "unsigned short", \
    int: "int", \
    unsigned int: "unsigned int", \
    long: "long", \
    unsigned long: "unsigned long", \
    long long: "long long", \
    unsigned long long: "unsigned long long", \
    float: "float", \
    double: "double", \
    long double: "long double", \
    char *: "string", \
    const char *: "const string", \
    void *: "void pointer", \
    const void *: "const void pointer", \
    default: "unknown" \
)

#endif

/* sample code 
#include <stdio.h>
#include "type_name.h"

int main() {
    int i = 10;
    float f = 1.5f;
    const char *str = "Bandhu";
    char ch = 'B';
    unsigned long long big = 999999999;
    _Bool flag = 1;

    printf("i is of type %s\n", TYPE_NAME(i));
    printf("f is of type %s\n", TYPE_NAME(f));
    printf("str is of type %s\n", TYPE_NAME(str));
    printf("ch is of type %s\n", TYPE_NAME(ch));
    printf("big is of type %s\n", TYPE_NAME(big));
    printf("flag is of type %s\n", TYPE_NAME(flag));

    return 0;
}
*/