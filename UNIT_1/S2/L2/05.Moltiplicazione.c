#include <stdio.h>

int main () {

    int a ;
    int b;
    int prodotto; 
     
    printf (" Calcolatrice per moltiplicazioni : \n "); 
    printf("Inserisci primo numero. \n ");
    scanf("%d", &a);

      printf("Inserisci secondo numero. \n ");
    scanf("%d", &b);

    prodotto = a * b;

    printf(" Il risultato della moltiplicazione è di %d" , prodotto); 
    printf(" \n  Se moltiplico %d per %d  il risultato sarà di %d" ,a ,b ,prodotto);

    return 0; 
}