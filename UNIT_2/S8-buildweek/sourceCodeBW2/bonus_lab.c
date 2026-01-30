#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10 // Define the safe limit constant

void run_vulnerable() {
    int vector[MAX_SIZE];
    int i;
    
    printf("\n--- VULNERABLE MODE ---\n");
    printf("I will let you enter 100 numbers into a size-10 array.\n");
    printf("Prepare for Segmentation Fault...\n");
    
    // VULNERABILITY: Loop goes to 100, buffer is only 10
    for (i = 0; i < 100; i++) {
        printf("Input [%d]: ", i+1);
        scanf("%d", &vector[i]); 
    }
}

void run_secure() {
    int vector[MAX_SIZE];
    int i, j, k, swap_var;
    int input_count = 0;
    
    printf("\n--- SECURE MODE ---\n");
    printf("Please enter up to %d integers.\n", MAX_SIZE);
    
    // SECURE INPUT CONTROL
    for (i = 0; i < MAX_SIZE; i++) {
        printf("Input [%d]: ", i+1);
        // We strictly use MAX_SIZE in the loop condition
        if (scanf("%d", &vector[i]) != 1) {
            printf("Invalid input detected.\n");
            break; // Handle non-integer input
        }
        input_count++;
    }

    // Bubble Sort (Only sorting what was actually input)
    for (j = 0; j < input_count - 1; j++) {
        for (k = 0; k < input_count - j - 1; k++) {
            if (vector[k] > vector[k+1]) {
                swap_var = vector[k];
                vector[k] = vector[k+1];
                vector[k+1] = swap_var;
            }
        }
    }

    printf("\nSorted Vector:\n");
    for (j = 0; j < input_count; j++) {
        printf("[%d]: %d\n", j+1, vector[j]);
    }
}

int main() {
    int choice;

    printf("==================================\n");
    printf("   BOF Lab - Day 3 Assignment     \n");
    printf("==================================\n");
    printf("1. Run Vulnerable Code (Crash)\n");
    printf("2. Run Secure Code (Input Control)\n");
    printf("Choose: ");
    scanf("%d", &choice);

    switch(choice) {
        case 1:
            run_vulnerable();
            break;
        case 2:
            run_secure();
            break;
        default:
            printf("Invalid selection.\n");
            break;
    }

    return 0;
}