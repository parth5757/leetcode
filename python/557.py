# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.


# class Solution:
#     def reverseWords(self, s: str) -> str:
#         words = s.split()# Step 1: Split the string into a list of words
#         # Step 2: Iterate through the words and reverse those with whitespace
#         for i in range(len(words)):
#             if ' ' in words[i]:
#                 # Split the word into parts based on whitespace
#                 word_parts = words[i].split(' ')
#                 # Reverse the parts and join them with a space
#                 reversed_word = ' '.join(reversed(word_parts))
#                 words[i] = reversed_word

#         # Step 3: Join the list of words back into a string
#         result_string = ' '.join(words)
        
#         return result_string

# # Example usage:
# p = Solution()
# s = "Hello world apple banana"
# result = p.reverseWords(s)
# print(result)  # Output: "olleH world elppa banana"

# class Solution:
#     def reverseWords(self, s: str) -> str:
#         char_list = list(s)# Step 1: Convert the string into a list of characters

#         # Step 2: Identify word boundaries based on whitespace
#         word_start = 0
#         for i in range(len(char_list)):
#             if char_list[i] == ' ':
#                 # Found a word boundary, reverse the word
#                 word_end = i - 1
#                 while word_start < word_end:
#                     char_list[word_start], char_list[word_end] = char_list[word_end], char_list[word_start]
#                     word_start += 1
#                     word_end -= 1
#                 # Move the word_start to the next character
#                 word_start = i + 1

#         # Step 3: Convert the list of characters back into a string
#         result_string = ''.join(char_list)

#         return result_string

# # Example usage:
# s = "Hello world apple banana"
# p = Solution()
# result = p.reverseWords(s)
# print(result)  # Output: "olleH world elppa banana"



class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the input string into words using space as a delimiter
        words = s.split(" ")
        
        # Initialize an empty list to store the reversed words
        reversed_words = []
        
        # Iterate through each word
        for word in words:
            # Reverse the characters in the word and add it to the list
            reversed_word = word[::-1]
            reversed_words.append(reversed_word)
        
        # Join the reversed words back together with spaces in between
        result = " ".join(reversed_words)
        
        return result
