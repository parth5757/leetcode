# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

# Example 1:

# Input: rowIndex = 3
# Output: [1,3,3,1]
# Example 2:

# Input: rowIndex = 0
# Output: [1]
# Example 3:

# Input: rowIndex = 1
# Output: [1,1]
 

# Constraints:

# 0 <= rowIndex <= 33
 

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

class Solution(object):
    # def getRow(self, rowIndex):
    #     """
    #     :type rowIndex: int
    #     :rtype: List[int]
    #     """
    #     row = [1] * (rowIndex + 1) 
    #     print(row)
    #     # main_list = []
    #     # for i in range(rowIndex + 1):
    #     #     print("i:", i)
    #     #     for j in range(i):
    #     #         print("j:", j)
    #     #         main_list.append([j])
    def getRow(self, rowIndex):
        # Initialize the row with 1s
        row = [1] * (rowIndex + 1) 
        print("main row:", row)
        # print(row)
        # Calculate each element of the row based on the previous row
        for i in range(rowIndex + 1):
            print("i:", i)
            for j in range(i - 1, 0, -1):
                print("before row:", row)
                print(j)
                row[j] = row[j] + row[j - 1]
                print("after row:", row)
        # return row
        return 0



num_row = int(input("Enter number of input: "))
sol = Solution()
print(sol.getRow(num_row))