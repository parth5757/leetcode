# Group anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.





# My Solution which is working but it exceed the time limit when test case size is big
class Solution(object):
    def bubble_sort(self, word):
        word = list(word)
        for i in range(len(word)):
            for j in range(len(word) - 1):
                if word[j] > word[j+1]:
                    word[j], word[j+1] = word[j+1], word[j]
        return ''.join(word)
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        n = len(strs) 
        ans = []
        strs = strs[::-1]
        for i in range(n):
            # print(i)
            iner_ans = [strs[i]]
            check_1 = self.bubble_sort(strs[i])
            if any (strs[i] in sublist for sublist in ans):
                continue
            else:
                for j in range(i+1, n):
                    check_2 = self.bubble_sort(strs[j])
                    check_2 = sorted(strs[j])
                    if check_1 == check_2:
                        iner_ans.append(strs[j])
                        # print(iner_ans)
                    # print(strs[i], strs[j])
                ans.append(iner_ans)
        return ans
        
sol = Solution()    
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))



# # Other Solution
# class Solution(object):
#     def groupAnagrams(self, strs):
#         anagram_map = {}
#         for word in strs:
#             sorted_word = ''.join(sorted(word))

#             if sorted_word not in anagram_map:
#                 anagram_map[sorted_word] = []
#             anagram_map[sorted_word].append(word)
#         return list(anagram_map.values())
    
# sol = Solution()    
# strs = ["eat","tea","tan","ate","nat","bat"]
# print(sol.groupAnagrams(strs))