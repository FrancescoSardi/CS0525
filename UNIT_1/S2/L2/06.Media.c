#include <stdio.h>

int main (){

    int a;
    int b;
    double media;

    printf("Calcolatore di media: \n ");

    printf(" \n Inserisci il primo numero della media: \n ");
    scanf("%d" , &a);

    printf(" \n Inserisci il secondo numero della media:  \n ");
    scanf("%d" ,  &b );

    media = (a +b)/2;

    printf("La media tra il numero %d e il numero %d è di %1.f " ,  a, b, media); 


    return 0 ; 

}