#include <stdio.h>

int main()
{
    int size_of_char = sizeof(char);
    int size_of_short = sizeof(short);
    int size_of_int = sizeof(int);
    int size_of_long = sizeof(long);
    int size_of_pointer = sizeof(void*);
    int size_of_float = sizeof(float);
    int size_of_double = sizeof(double);
    int size_of_longdouble = sizeof(long double);

    printf("char: %d\n", size_of_char);
    printf("short: %d\n", size_of_short);
    printf("int: %d\n", size_of_int);
    printf("long: %d\n", size_of_long);
    printf("pointer: %d\n", size_of_pointer);
    printf("float: %d\n", size_of_float);
    printf("double: %d\n", size_of_double);
    printf("long double: %d\n", size_of_longdouble);

    return 0;
}
