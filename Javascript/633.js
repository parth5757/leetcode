/**
 * @param {number} c
 * @return {boolean}
 */
var judgeSquareSum = function(c) {
    let left = 0;
    let right = Math.floor(Math.sqrt(c));
    while (left <= right) {
        current_sum = left * left + right * right;
        // console.log(current_sum)
        if(current_sum == c){
            return true;
        } else if(current_sum < c){
            left++;
        }
        else{
            right--;
        }
    }
    return false;
};

console.log(judgeSquareSum(8));