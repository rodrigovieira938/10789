#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
    if(argc <= 1) return 0;
    int fullSpace = 5;

    size_t lenght = strlen(argv[1]);
    for(int i = 0; i < lenght + fullSpace * 2 + 2; i++) {
        printf("*");
    }
    printf("\n*");
    for(int i = 0; i < fullSpace; i++) {
        printf(" ");
    }
    printf("%s", argv[1]);
    for(int i = 0; i < fullSpace; i++) {
        printf(" ");
    }
    printf("*\n");
    for(int i = 0; i < lenght + fullSpace * 2 + 2; i++) {
        printf("*");
    }
    printf("\n");
}