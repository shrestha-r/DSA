#include <stdio.h>

void main(){
    int i =1, n = 10;
    do{
        printf("%d is square of %d\n",i,i*i);
        i++;
    }while(i!=n+1);
}