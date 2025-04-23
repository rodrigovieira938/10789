#include <stdio.h>

int main() {
    int segundos = 0, minutos = 0, horas = 0;

    printf("Introduza o tempo em segundos: ");
    scanf("%d", &segundos);

    minutos = segundos / 60;
    segundos %= 60;
    horas = minutos / 60;
    minutos %= 60;

    horas %= 24;

    printf("O tempo é igual a %d:%d:%d\n", horas, minutos, segundos);

    return 0;
}