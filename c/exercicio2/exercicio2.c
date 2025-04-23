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
    int num3;

    printf("Introduza o primeiro número: ");
    scanf("%d", &num1);
    printf("Introduza o segundo número: ");
    scanf("%d", &num2);
    printf("Introduza o terceiro número: ");
    scanf("%d", &num3);

    int max_num = max(num3,max(num1,num2));
    int min_num = min(num3,min(num1,num2));

    if(max_num == num1) {
        printf("O número máximo é o primeiro (%i)\n", max_num);
    } else if(max_num == num2) {
        printf("O número máximo é o segundo (%i)\n", max_num);
    } else if(max_num == num3) {
        printf("O número máximo é o terceiro (%i)\n", max_num);
    }


    if(max_num == num1) {
        printf("O número mínimo é o primeiro (%i)\n", min_num);
    } else if(min_num == num2) {
        printf("O número mínimo é o segundo (%i)\n", min_num);
    } else if(min_num == num3) {
        printf("O número mínimo é o terceiro (%i)\n", min_num);
    }

    return 0;
}