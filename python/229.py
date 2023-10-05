# 229. Majority Element II
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]
 

# Constraints:

# 1 <= nums.length <= 5 * 104
# -109 <= nums[i] <= 109

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        item = []
        same = set()
        total = 0
        for i in nums:
            item.append(i)
            for j in item:
                if i == j:
                    same.add(i)
                else:
                    pass
        print(same)
        
p = Solution()
nums = [3,2,3]
print(p.majorityElement(nums))


# class Solution:
#     def majorityElement(self, nums: list[int]) -> list[int]:
#         if len(nums) == 1:
#             print(nums)
#         elif len(nums) == 2:
#             print(nums)
#         elif len(nums) == 3:
            