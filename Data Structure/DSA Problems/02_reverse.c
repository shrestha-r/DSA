#include <stdio.h>

void main(){
    int array[] = {3,2,5,4,1};
    // int j = sizeof(array)/sizeof(array[0]) -1 ;
    int temp[5];
    // printf("%d\n",j);
    // for (int i =0;i<5;i++){
    //     temp[i] = array[j];
    //     printf("j=%d,i=%d\n",j,i);
    //     j--;
    // }
    // for(int i=0;i<5;i++){
    //     printf("%d,",temp[i]);
    // }

    // Solution 

    int n = sizeof(array)/sizeof(array[0])-1;

    for (int i=0;i<n+1;i++){
        temp[i] = array[n-i];
    }
      for(int i=0;i<n+1;i++){
        printf("%d,",temp[i]);
    }
}



// ## Solution

