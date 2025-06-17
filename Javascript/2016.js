/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumDifference = function(nums) {
    let ans = -1
    const n = nums.length
    for (let i = 0; i < n; i++){
        for(let j = i+1; j < n; j++){
            // console.log(i, j);
            if(nums[i] < nums[j]){
                let diff = nums[j]-nums[i]
                if(diff>ans){
                    ans = diff;
                }
            }
        }
    }
    return ans; 
};

nums = [7,1,5,4]
// nums = [9,4,3,2]
// nums = [1,5,2,10]
console.log(maximumDifference(nums))