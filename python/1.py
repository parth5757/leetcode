# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# class solution(object):
#     def twoSum(self, nums, target):
#         ans = []
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j]== target:
#                     # print(i , j)
#                     ans.extend([i, j])
#         return ans

# num1 = [7, 4, 2 ,8]
# tar = 9
# sol = solution()
# print(sol.twoSum(num1, tar))
    
class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        i = 0
        while i < len(nums) - 1:
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
        return []


num1 = [7, 4, 2 ,8]
tar = 9
sol = Solution()
print(sol.twoSum(num1, tar))