#include <stdio.h>

int main () {
    int vector[10], i, j, k;
    int swap_var;

    /* printf("Inserire 10 interi:\n");

    // Input loop - Hardcoded to 10
    for (i = 0 ; i < 10 ; i++) {
        int c = i+1;
        printf("[%d]:", c);
        scanf("%d", &vector[i]);
    } */

    printf("Inserire interi (VULNERABLE LOOP):\n");

    // MODIFICATION: Loop runs 100 times, but array only holds 10!
    for ( i = 0 ; i < 100 ; i++) 
    {
        int c= i+1;
        printf("[%d]:", c);
        // This will eventually write past the end of 'vector'
        scanf ("%d", &vector[i]); 
    }

    printf("Il vettore inserito e':\n");
    for (i = 0 ; i < 10 ; i++) {
        int t = i+1;
        printf("[%d]: %d\n", t, vector[i]);
    }

    // Bubble sort algorithm
    for (j = 0 ; j < 10 - 1; j++) {
        for (k = 0 ; k < 10 - j - 1; k++) {
            if (vector[k] > vector[k+1]) {
                swap_var = vector[k];
                vector[k] = vector[k+1];
                vector[k+1] = swap_var;
            }
        }
    }

    printf("Il vettore ordinato e':\n");
    for (j = 0; j < 10; j++) {
        int g = j+1;
        printf("[%d]: %d\n", g, vector[j]);
    }

    return 0;
}