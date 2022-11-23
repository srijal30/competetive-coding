#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
    int count, sum, ctr = 0;
    char buf[800], *tmp;

        //get first line
        fgets(buf, 800, stdin);
        sscanf(buf, "%d %d", &count, &sum);
    int* arr = (int*)malloc(sizeof(int)*count);

        //get second line
    fgets(buf, 800, stdin);
        tmp = strtok(buf, " ");
        while(tmp != NULL){
                sscanf(tmp, "%d", arr + ctr++);
                arr[ctr-1]--;
                tmp = strtok(NULL, " ");
        }

    //actual code
    int* memo = (int*)calloc(sum, sizeof(int));
    for(int i = 0; i < sum; i++) memo[i] = -1;

    //for every coin establish it as 1
    for(int i = 0; i < count; i++){
        if(arr[i] <= sum) memo[arr[i]] = 1;
    }


        for(int i = 0; i < sum; i++){
                if(memo[i] == -1) continue;
                //for all the coins
                for(int coin = 0; coin < count; coin++){
                        int nextSum = i + arr[coin];
                        int steps = memo[i] + 1;
                        if(nextSum < sum){
                                //we have to change
                                if(memo[nextSum] == -1) memo[nextSum] = steps;
                                //we should change cuz its lower
                                else if(memo[nextSum] > steps) memo[nextSum] = steps;
                        }
                }
        }

    printf("%d\n", memo[sum-1]);

    free(arr); free(memo);
    return 0;
}