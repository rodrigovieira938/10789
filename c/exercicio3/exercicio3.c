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
    int num1 = 0, num2 = 0;
    int max_num = 0, min_num = 0;

    printf("Introduze o primeiro número: ");
    scanf("%d", &num1);

    printf("Introduze o segundo número: ");
    scanf("%d", &num2);

    max_num = max(num1,num2);
    min_num = min(num1,num2);

    printf("Crescente: %d, %d\n", min_num, max_num);

    printf("Descrecente: %d, %d\n", max_num, min_num);

    return 0;
}