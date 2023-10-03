# 1512. Number of Good Pairs

# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100/

# Not Working
# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         pair = []

#         # Iterate through the list
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 # Compare nums[i] with nums[j]
#                 if nums[i] == nums[j]:
#                     pair.append([nums[i], nums[j]])
#         print(len(pair))
#         print(pair)

class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        n = len(nums)
        pairs = []  # Initialize an empty list to store pairs

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    pairs.append([i, j])
        # print(pairs)
        return len(pairs)
        

# Test case
nums = [1, 2, 3, 1, 1, 3]
solution = Solution()
result = solution.numIdenticalPairs(nums)
print("Number of identical pairs:", result)
# print(pairs)
        