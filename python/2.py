# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        val1 = int(''.join(map(str ,l1)))
        print("val1", val1)
        Val1 = int(str(val1)[::-1])
        print("Val1", Val1)
        val2 = int(''.join(map(str, l2)))
        print("val2", val2)
        Val2 = int(str(val2)[::-1])
        print("Val2", Val2)

        total = Val1 + Val2
        print("total", total)
        Total = int(str(total)[::-1])

        return list(str(Total))


sol = Solution()
print(sol.addTwoNumbers(l1=[2,4,3], l2=[5,6,4]))
print(sol.addTwoNumbers(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]))












        
#         val1 = int(''.join(map(str, l1)))
#         val2 = int(''.join(map(str, l2)))
#         total = val1 + val2
#         ans = [int(x) for x in str(total)]
#         ans.reverse()
#         return ans

# sol = Solution()
# print(sol.addTwoNumbers(l1=[2,4,3], l2=[5,6,4]))