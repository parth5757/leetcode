// 557. Reverse Words in a String III
// Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

// Example 1:

// Input: s = "Let's take LeetCode contest"
// Output: "s'teL ekat edoCteeL tsetnoc"
// Example 2:

// Input: s = "God Ding"
// Output: "doG gniD"
 

// Constraints:

// 1 <= s.length <= 5 * 104
// s contains printable ASCII characters.
// s does not contain any leading or trailing spaces.
// There is at least one word in s.
// All the words in s are separated by a single space.

var reverseWords = function(s) {
    // Split the input string into words using space as a delimiter
    const words = s.split(" ");
    
    // Initialize an empty array to store the reversed words
    const reversedWords = [];
    
    // Iterate through each word
    for (const word of words) {
        // Reverse the characters in the word and add it to the array
        const reversedWord = word.split('').reverse().join('');
        reversedWords.push(reversedWord);
    }
    
    // Join the reversed words back together with spaces in between
    return reversedWords.join(" ");
};

const input = "Let's take LeetCode contest";
const result = reverseWords(input);
console.log(result);
