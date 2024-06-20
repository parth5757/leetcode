# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

# Failed Attempt
# class Solution:
#     def singleNumber(self, nums):
#         num_dict = {}
#         for i in nums:
#             if i == num_dict.keys:
#                 print("hello")
#                 num_dict.values() + 1
#             else:
#                 num_dict[i] = 1
#         print(num_dict)
#         for key, value in num_dict.items():
#             if value == 1:
#                 return key
            
# num = [4,1,2,1,2]
# sol = Solution()
# print(sol.singleNumber(num))



class Solution:
    def singleNumber(self, nums):
        num_dict = {}
        for i in nums:
            if i == num_dict:
                num_dict[i] +=1
            else:
                num_dict[i] = 1
        
        for key, value in num_dict.items():
            if value == 1:
                return key
            
num = [4,1,2,1,2]
sol = Solution()
print(sol.singleNumber(num))
