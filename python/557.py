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

class Solution:
    def reverseWords(self, s: str) -> str:
        words = input_string.split()# Step 1: Split the string into a list of words
        # Step 2: Iterate through the words and reverse those with whitespace
        for i in range(len(words)):
            if ' ' in words[i]:
                # Split the word into parts based on whitespace
                word_parts = words[i].split(' ')
                # Reverse the parts and join them with a space
                reversed_word = ' '.join(reversed(word_parts))
                words[i] = reversed_word

        # Step 3: Join the list of words back into a string
        result_string = ' '.join(words)
        
        return result_string

# Example usage:
input_string = "Hello world apple banana"
result = reverse_words_with_whitespace(input_string)
print(result)  # Output: "olleH world elppa banana"