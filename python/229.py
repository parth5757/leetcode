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


# an hard try of your but unfortunately it is not work
# class Solution:
#     def majorityElement(self, nums: list[int]) -> list[int]:
#         if len(nums) == 1:
#             print(nums)
#         elif len(nums) == 2:
#             print(nums)
#         elif len(nums) == 3:
#             item = []
#             same = set()
#             total = []
#             for i in nums:
#                 item.append(i)
#                 for j in item:
#                     if i == j:
#                         same.add(i)
#                     else:
#                         pass
#             # print(same)
#             for i in nums:
#                 for j in same:
#                     if i != j:
#                         total.append(i)
#                     else:
#                         pass
#             print(total)
#         else:
#             print("Fuck of leetcode")
# p = Solution()
# nums = [3,2,6]
# print(p.majorityElement(nums))

# not use in leetcode
# class Solution:
#     def majorityElement(self, nums: list[int]) -> list[int]:
#         if len(nums) < 3:
#             # If there are 1 or 2 elements, all of them appear more than n/3 times.
#             return nums
        
#         num1, num2 = None, None
#         count1, count2 = 0, 0
        
#         for num in nums:
#             if num == num1:
#                 count1 += 1
#             elif num == num2:
#                 count2 += 1
#             elif count1 == 0:
#                 num1, count1 = num, 1
#             elif count2 == 0:
#                 num2, count2 = num, 1
#             else:
#                 count1 -= 1
#                 count2 -= 1
        
#         count1, count2 = 0, 0
        
#         for num in nums:
#             if num == num1:
#                 count1 += 1
#             elif num == num2:
#                 count2 += 1
        
#         result = []
#         if count1 > len(nums) // 3:
#             result.append(num1)
#         if count2 > len(nums) // 3:
#             result.append(num2)
        
#         return result

# p = Solution()
# nums = [3,2,3]
# print(p.majorityElement(nums))


class Solution:
  def majorityElement(self, nums: list[int]) -> list[int]:
    ans1 = 0
    ans2 = 1
    count1 = 0
    count2 = 0

    for num in nums:
      if num == ans1:
        count1 += 1
      elif num == ans2:
        count2 += 1
      elif count1 == 0:
        ans1 = num
        count1 = 1
      elif count2 == 0:
        ans2 = num
        count2 = 1
      else:
        count1 -= 1
        count2 -= 1

    return [ans for ans in (ans1, ans2) if nums.count(ans) > len(nums) // 3]
