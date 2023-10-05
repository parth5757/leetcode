// 229. Majority Element II
// Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

// Example 1:

// Input: nums = [3,2,3]
// Output: [3]
// Example 2:

// Input: nums = [1]
// Output: [1]
// Example 3:

// Input: nums = [1,2]
// Output: [1,2]
 

// Constraints:

// 1 <= nums.length <= 5 * 104
// -109 <= nums[i] <= 109
/**
 * @param {number[]} nums
 * @return {number[]}
 */
var majorityElement = function(nums) {
    let ans1 = 0;
    let ans2 = 1;
    let count1 = 0;
    let count2 = 0;

    for (let num of nums) {
        if (num === ans1) {
            count1++;
        } else if (num === ans2) {
            count2++;
        } else if (count1 === 0) {
            ans1 = num;
            count1 = 1;
        } else if (count2 === 0) {
            ans2 = num;
            count2 = 1;
        } else {
            count1--;
            count2--;
        }
    }

    let result = [];
    const n = nums.length;

    if (nums.filter(num => num === ans1).length > n / 3) {
        result.push(ans1);
    }
    if (nums.filter(num => num === ans2).length > n / 3) {
        result.push(ans2);
    }

    return result;
};

// Example usage:
const nums = [2, 2];
console.log(majorityElement(nums)); // Output: [2]

