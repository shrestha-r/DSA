#include <stdio.h>

void main(){
    int row =5, column = 10;
    for(int i = 1;i<=row;i++){
        for(int j =1;j<=i;j++){
            printf("*");
        }
        for(int s =1;s<=column - (i*2);s++){
            printf(" ");
        }
        for(int j = 1;j<=i;j++){
            printf("*");
        }
        printf("\n");
    }
    int j;
    for (int i=4;i>=1;i--){
        for(j=1;j<=i;j++){
            printf("*");
        }
        for(int s=1;s<=column - ((j-1)*2);s++){
            printf(" ");
        }
        for(int k=1;k<=i;k++){
            printf("*");
        }
        printf("\n");
    }
}