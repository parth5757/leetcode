# You are given a string s and an integer k. Your task is to find the maximum difference between the frequency of two characters, freq[a] - freq[b], in a substring subs of s, such that:

# subs has a size of at least k.
# Character a has an odd frequency in subs.
# Character b has an even frequency in subs.
# Return the maximum difference.

# Note that subs can contain more than 2 distinct characters.

 

# Example 1:

# Input: s = "12233", k = 4

# Output: -1

# Explanation:

# For the substring "12233", the frequency of '1' is 1 and the frequency of '3' is 2. The difference is 1 - 2 = -1.

# Example 2:

# Input: s = "1122211", k = 3

# Output: 1

# Explanation:

# For the substring "11222", the frequency of '2' is 3 and the frequency of '1' is 2. The difference is 3 - 2 = 1.

# Example 3:

# Input: s = "110", k = 3

# Output: -1

class Solution(object):
    def maxDifference(self, s, k):
        # Basic Constraints

        # 3 <= s.length <= 3 * 10^4
        if (len(s)<3 or len(s) > 3 * (10 ** 4)):
            return "Sorry substring is not as required length in between 3 to 10^4"
        # s consists only of digits '0' to '4'.
        allow_digit = [0, 1, 2, 3, 4]
        sub_strings = set(s)
        for i in sub_strings:
            if(int(i) not in allow_digit):
                return f"sorry this substring contain this digit {i} which is not allow"
            else:
                pass
        # The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
        # this condition check at the code area because at there we get all character frequency. at the line number 102
        # 1 <= k <= s.length      same as the one another condition given in the problem where  # subs has a size of at least k.
        if(1 <= k <= len(s)):
            pass
        else:
            return f"k size is not more then the substrings total size {len(s)}"
        

        # Note that subs can contain more than 2 distinct characters.
        distinct = len(set(s))
        if (distinct < 2):
            return "Sorry it can't contain the 2 or more then 2 number of distinct character"
        
        # code work get started here

        # let's start with the consecutive frequency
        char_freq = []
        count = 1
        for i in range(1, len(s)):
            if (s[i] == s[i-1]):
                count += 1
            else:
                char_freq.append(s[i-1] * count)
                count = 1
        char_freq.append(s[-1] * count)
        # print(char_freq)
        
        # find the maximum consecutive odd and even frequency
        max_odd = 0
        max_even = 0
        for i in char_freq:
            if(len(i)%2==0):
                # print(len(i), max_even)
                if (len(i) > max_even):
                    max_even = len(i)
                pass
                # max_even.append(i)
                # print(len(i))
            else:
                # print(len(i), max_odd)
                if(len(i) > max_odd):
                    max_odd = len(i)
                pass
                # max_odd.append(i)
                # print(len(i))
        # print(f"max odd frequency is {max_odd}")
        # print(f"max even frequency is {max_even}")

        # check that both even and odd 
        if max_even == 0 or max_odd == 0:
            return -1
        
        result = max_odd - max_even
        print(max_odd, max_even)
        return result

s = Solution()
# print(s.maxDifference("12233", 5))
# print(s.maxDifference("1122211", 3))
# print(s.maxDifference("110", 3))
# print(s.maxDifference("2421", 1))
# print(s.maxDifference("2222130", 2))
print(s.maxDifference("02024404", 6))
# print(s.maxDifference("4240100144", 10))