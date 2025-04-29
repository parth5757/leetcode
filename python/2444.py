'''
Count Subarrays With Fixed Bounds
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.
'''
import time
import tracemalloc
# method 1
print("method 1")
# brute force approach (too much time and memory(space) consuming and not suitable for the large dataset.)
# time and space complexity of this code is O(n)
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        def min_max(arr, minV, maxV):
            if minV in arr and maxV in arr and min(arr) >= minV and max(arr) <= maxV:
                return True
            else:
                return False
        n = len(nums)
        sub_arr = []
        for i in range(n):
            for j in range(i, n):
                sub_sub_arr = []
                for k in range(i, j+1):
                    # print(arr[k], end=" ")
                    # if(arr[k] == 1):
                    sub_sub_arr.append(nums[k])
                # print(sub_sub_arr)
                sub_arr.append(sub_sub_arr)
        # print("sub array is: ", sub_arr)
        # print("total number of possible sub array is: ", len(sub_arr))
        count = 0
        for i in sub_arr:
            if min_max(i, minK, maxK) == True:
                # print(i)
                count += 1
        # print(count)
        return count
# arr = [1,2,3,4,5]
# arr = [1,3,5,2,4,5]
arr = [1,3,5,2,7,5]

sol = Solution()

print(sol.countSubarrays(arr, 2, 5))


# method 2
class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        start = time.time()
        tracemalloc.start()        
        count = 0
        minpos = maxpos = -1
        left_bound = -1
        for i, num in enumerate(nums):
            # print(i, num)
            if num < minK or num > maxK:
                left_bound = i
                # print(left_bound, num)
            if num == minK:
                minpos = i
            if num == maxK:
                maxpos = i
            # print(minpos, maxpos, left_bound)
            # print("2: ", count, max(0, min(minpos, maxpos)-left_bound), min(minpos, maxpos)-left_bound)
            count += max(0, min(minpos, maxpos)-left_bound)

        # Calculate space complexity
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"- Current memory usage: {current / 1024:.2f} KB")
        print(f"- Peak memory usage: {peak / 1024:.2f} KB")
        print(time.time()-start)
        return count
    
# arr = [1,3,5,2,4,5]
arr = [1,3,5,2,7,5]
# arr = [1,2,3,4,5]

sol = Solution()
print("method 2")

print(sol.countSubarrays(arr, 2, 5))