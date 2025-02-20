#include <stdio.h>

int main() {
    int segundos;

    printf("Introduza o tempo em segundos: ");
    scanf("%d", &segundos);

    int minutos = segundos / 60;
    segundos %= 60;
    int horas = minutos / 60;
    minutos %= 60;

    printf("O tempo é igual a %d:%d:%d\n", horas, minutos, segundos);

    return 0;
}