# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

# Example 1:

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:

# Input: c = 3
# Output: false
 

# Constraints:

# 0 <= c <= 231 - 1


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # squaresum = []
        # if c > 4:
        #     for i in range(c):
        #         val =(i+1) ** 2
        #         print(val)                
        #         squaresum.append(squaresum[0]+val)
        #         if squaresum == c:
        #             return True
        #         elif squaresum < c:
        #             continue
        #         else:
        #             return False
        # else:
        #     return False

        left, right = 0, int(c ** 0.5)
        # print(left, right)
        
        while left <= right:
            current_sum = left ** 2 + right ** 2
            # print("Square nuber is:", left, right, current_sum)
            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
                
        return False
c = int(input("Enter the number"))
a = Solution()
print(a.judgeSquareSum(c))