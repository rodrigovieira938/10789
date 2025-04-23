#include <stdio.h>

int main() {
    float saldo_inicial, cheque;

    printf("Introduza o saldo inicial: ");
    scanf("%f", &saldo_inicial);

    printf("Introduza o valor do cheque em análise: ");
    scanf("%f", &cheque);

    if(saldo_inicial < cheque) {
        printf("O saldo não pode ser descontado\n");
    } else {
        printf("O saldo pode ser descontado. O saldo agora é %2f\n", saldo_inicial-cheque);
    }

    return 0;
}