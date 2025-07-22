class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        digit = str(n)
        addition = 0
        multiplication = 1
        for i in digit:
            addition = addition + int(i)
            multiplication = multiplication * int(i)

        total = addition + multiplication
        if(total==n):
            return True
        else:
            if n % total == 0:
                return True
            return False
            

s = Solution()
n = int(input("Enter number you want to enter it: "))
print(s.checkDivisibility(n))