# not working 
# # nums = [21, 50, 75, 11]
# nums = [7,1,5,4]
# num_idx = []
# prob_ans = {}
# ans = 0
# for i in range(len(nums)):
#     num_idx.append(i)
# # print(num_idx)
# for i in range(len(nums)):
#     for j in num_idx:
#         if j != i:
#             # print("i is", i, "j is", j)
#             result = nums[i]-nums[j]
#             prob_ans[(nums[i], nums[j])] = result
#         else:
#             pass
# print(prob_ans)
# for key, val in prob_ans.items():
#     if key[0] < key[1]:
#         print(key)
#         if val > ans:
#             ans = val
#             # print(ans)
#         else:
#             pass
#     else:
#         pass
# print(ans)

class Solution(object):
    def maximumDifference(self, nums):
        prob_ans = {}
        ans = -1
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    result = nums[j]-nums[i]
                    prob_ans[(nums[i], nums[j])] = result
        # print(prob_ans)
        for key, val in prob_ans.items():
            if val > ans:
                ans = val
                # print(ans)
        return ans
nums = [7,1,5,4]
nums = [1,5,2,10]
nums = [9,4,3,2]
s = Solution()
print(s.maximumDifference(nums))


# smaller and faster code compare to my previous code.
class Solution(object):
    def maximumDifference(self, nums):
        ans = -1
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    if diff > ans:
                        ans = diff
        return ans

nums = [7,1,5,4]
nums = [1,5,2,10]
nums = [9,4,3,2]
s = Solution()
print(s.maximumDifference(nums))