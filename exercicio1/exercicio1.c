#include <stdio.h>

int main() {
    int num = 0;
    for(int i = 0; i < 10; i++) {
        num+=2;
        printf("Num = %d, i = %d", num, i);
        printf("Aqui FOR");
    }

    return 0;
}