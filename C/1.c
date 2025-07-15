// num1 = [7, 4, 2 ,8]
// tar = 9

#include<stdio.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    static int result[2];
    for(int i=0; i<numsSize; i++){
        for(int j=i+1; j<numsSize; j++){
            if(nums[i] + nums[j] == target){
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}

int main() {
    int nums[] = {7,4,2,8};
    int target = 9;
    int numsSize = sizeof(nums) / sizeof(nums[0]);
    int returnSize;
    int* indices = twoSum(nums, numsSize, target, &returnSize);
    if(indices != NULL && returnSize == 2){
        printf("Indices: %d, %d\n", indices[0], indices[1]);
    } else {
        printf("No solution found.\n");
    }
    return 0;
}