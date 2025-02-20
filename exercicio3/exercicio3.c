#include <stdio.h>

int max(int a, int b) {
    if(a > b)
        return a;
    return b;
}
int min(int a, int b) {
    if(a < b)
        return a;
    return b;
}


int main() {
    int num1;
    int num2;

    printf("Introduze o primeiro número: ");
    scanf("%d", &num1);

    printf("Introduze o segundo número: ");
    scanf("%d", &num2);

    printf("Crescente:   ");

    int max_number = max(num1, num2);
    int min_number = min(num1, num2);

    for(int i = min_number; i <= max_number; i++) {
        printf("%d",i);
        if(i < max_number) {
            printf("; ");
        }
    }
    printf("\n");

    printf("Descrecente: ");


    for(int i = max_number; i >= min_number; i--) {
        printf("%d",i);
        if(i > min_number) {
            printf("; ");
        }
    }
    printf("\n");

    return 0;
}