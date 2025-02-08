# Example 1:

# Input: s = "aaaaabbc"

# Output: 3

# Explanation:

# The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
# The maximum difference is 5 - 2 = 3.
# Example 2:

# Input: s = "abcabcab"

# Output: 1

# Explanation:

# The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
# The maximum difference is 3 - 2 = 1.
 

# Constraints:

# 3 <= s.length <= 100
# s consists only of lowercase English letters.
# s contains at least one character with an odd frequency and one with an even frequency.

class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not (3 <= len(s) <= 100):
            return "s must contain at least 3 and at most 100 characters"
        if not s.islower():
            return "s all character must be in lowercase"
        
                # Manually count character frequencies
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # print(freq)
        
        # Extract odd and even frequency values
        odd_freq = [v for v in freq.values() if v % 2 == 1]
        even_freq = [v for v in freq.values() if v % 2 == 0]

        # Ensure at least one odd and one even frequency exists
        if odd_freq and even_freq:
            return max(odd_freq) - min(even_freq)
        else:
            return "Invalid input: need at least one odd and one even frequency"
sol = Solution()
# s = "abcabcab"
s = "aaaaabbc"
print(sol.maxDifference(s))