class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # val1 = int(''.join(map(str ,l1)))
        # Val1 = int(str(val1)[::-1])
        # val2 = int(''.join(map(str, l2)))
        # Val2 = int(str(val2)[::-1])

        # total = Val1 + Val2
        # Total = int(str(total)[::-1])

        # return list(str(Total))

        val1 = int(''.join(map(str, l1)))
        val2 = ""
        for num in l2:
            val2 += str(num)
        reversed_val1 = int(''.join([val for val in str(val1)][::-1]))
        reversed_val2 = int(''.join([val for val in str(val2)][::-1]))
        ans = reversed_val1 + reversed_val2
        return int(''.join([val for val in str(ans)][::-1]))
        
s = Solution()
print(s.addTwoNumbers([2,4,3], [5,6,4]))
print(s.addTwoNumbers(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]))