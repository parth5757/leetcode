// Check Divisibility by Digit Sum and Product
/*
You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:

The digit sum of n (the sum of its digits).

The digit product of n (the product of its digits).

Return true if n is divisible by this sum; otherwise, return false.

 

Example 1:

Input: n = 99

Output: true

Explanation:

Since 99 is divisible by the sum (9 + 9 = 18) plus product (9 * 9 = 81) of its digits (total 99), the output is true.

Example 2:

Input: n = 23

Output: false

Explanation:

Since 23 is not divisible by the sum (2 + 3 = 5) plus product (2 * 3 = 6) of its digits (total 11), the output is false.

 

Constraints:

1 <= n <= 106
*/

#include<stdio.h> // printf, sprintf
#include<stdbool.h>
#include<string.h> // strlen, strcpy
#include<math.h>
#include<stdlib.h>
#include "type_name.h"

bool checkDivisibility(int n) {
    char digit[10000];
    sprintf(digit, "%d", n);
    int addition = 0;
    int multiplication = 1;
    char int_digit[10000];
    strcpy(int_digit, digit);
    // printf("Type of int_digit is %s\n", TYPE_NAME(int_digit));
    for(int i=0;i<strlen(digit); i++){
        int int_digit_val = digit[i] - '0';
        // printf("%d\n", int_digit_val);
        addition = addition + int_digit_val;
        multiplication = multiplication * int_digit_val;
    }

    int total = addition + multiplication;
    printf("%d\n%d\n%d", addition, multiplication, total);
    if(total == n){
        return true;
    }
    else if(n % total == 0){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int n = 99;
    bool result = checkDivisibility(n);
    printf("\nResult: %s\n", result ? "true" : "false");
    return 0;
}