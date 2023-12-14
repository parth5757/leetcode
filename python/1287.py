# Element Appearing More Than 25% In Sorted Array

# Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

# Example 1:

# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# Example 2:

# Input: arr = [1,1]
# Output: 1
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 105
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = len(arr)
        total = {}
        for num in arr:
            if num in total:
                total[num] += 1
            else:
                total[num] = 1
        
        # Find the threshold value
        threshold = 0.25 * l

        # Filter values that meet the condition
        result_values = [key for key, value in total.items() if value >= threshold]

        # Return the value with the highest frequency
        return max(result_values, key=lambda x: total[x])

arr = [1, 2, 3, 3]
a = Solution()
print(a.findSpecialInteger(arr))
