#include <stdio.h>

void main(){
    printf("Quetion 1\n");
    int n = 10;
    for(int i=1; i<=n; i++){
        printf("%d\t",i);
    }
    printf("\n");

    int i = 1;
    while (i!=n+1){
        printf("%d\t",i);
        i++;
    }
    printf("\n");
    // printf("i = %d\n",i); Guess the value of i, here
    i = 1;
    do{
        printf("%d\t",i);
        i++;
    }while(i!=n+1);
    printf("\n");
}