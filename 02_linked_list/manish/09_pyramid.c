#include <stdio.h>

void main(){

    printf("pyramid pattern \n");
    int n = 5,k;
    for(int i=n;i>0;i--){
        for (k =1;k<=n-i;k++){
            printf(" ");
        }
        for(int j = i;j>0;j--){
            printf("%d",i);
        }
        printf("\n");
    }
}