#include <stdio.h>
#include <string.h>

#define MAX_CHAR 26

int maxDifference(char *s) {
    int n = strlen(s);
    
    // Constraint check
    if (n < 3 || n > 100) {
        printf("s must contain at least 3 and at most 100 characters\n");
        return -1;
    }

    // Frequency array to count occurrences of each character
    int freq[MAX_CHAR] = {0};
    
    // Count frequencies
    for (int i = 0; i < n; i++) {
        if (s[i] < 'a' || s[i] > 'z') {
            printf("s all characters must be in lowercase\n");
            return -1;
        }
        freq[s[i] - 'a']++;
    }

    // Find max odd and min even frequencies
    int max_odd = -1, min_even = 101;

    for (int i = 0; i < MAX_CHAR; i++) {
        if (freq[i] > 0) {
            if (freq[i] % 2 == 1) {
                if (freq[i] > max_odd) {
                    max_odd = freq[i];
                }
            } else {
                if (freq[i] < min_even) {
                    min_even = freq[i];
                }
            }
        }
    }

    // Ensure at least one odd and one even frequency exist
    if (max_odd != -1 && min_even != 101) {
        return max_odd - min_even;
    } else {
        printf("Invalid input: need at least one odd and one even frequency\n");
        return -1;
    }
}

int main() {
    char s[] = "aaaaabbc";  // Example input
    int result = maxDifference(s);
    if (result != -1) {
        printf("Output: %d\n", result);
    }
    return 0;
}
