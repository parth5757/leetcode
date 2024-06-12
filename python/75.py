# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

# You must solve this problem without using the library's sort function.

 

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]
 

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.
 

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
# working but not accepted in leetcode
#         red = []
#         white = []
#         blue = []
#         for i in nums:
#             if i == 0:
#                 red.append(i)
#             elif i == 1:
#                 white.append(i)
#             elif i == 2:
#                 blue.append(i)
#         return red + white + blue
    
# nums = [2,0,1]
# sol = Solution()
# print(sol.sortColors(nums))

# 2 approach 

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] >= nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

nums = [2,0,1]
sol = Solution()
print(sol.sortColors(nums))