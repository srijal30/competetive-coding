#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    unsigned long arr[] = {1, 2, 4, 8, 16, 32};
    if(n <= 6){printf("%lu\n", arr[n-1]); return 0;}
    
    for(int i = 0; i < n-6; i++){
        long sum = (arr[0] + arr[1] + arr[2] + arr[3] + arr[4] + arr[5]) % 1000000007;
        for(int l = 0; l < 5; l++) arr[l] = arr[l+1];
        arr[5] = sum;
    }

    printf("%lu\n", arr[5]);
}