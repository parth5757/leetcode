class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        if 1 <= n <= 1000 and 1 <= w <= 1000 and 1 <= maxWeight <= 10**9:
            # total number of available cells
            N = n * n
            Ans = 0
            for i in range(N):
                # I think here use while loop
                if (i+1) * w <= maxWeight:
                    Ans = 1 + i
                else:
                    break
            return Ans
        else:
            return "Entered values crossing limits"

sol = Solution()
n = 2
w = 3 
maxWeight = 15
print(sol.maxContainers(n, w, maxWeight))
n = 3
w = 5 
maxWeight = 25
print(sol.maxContainers(n, w, maxWeight))
