"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        N = len(prices)
        maxs = [0] * N
        for ix in range(N):
            if ix == 0:
                maxs[N-1] = prices[N-1]
                continue
            i, j = N - 1 - ix, N - ix
            if prices[i] > maxs[j]:
                maxs[i] = prices[i]
            else:
                maxs[i] = maxs[j]

        for ix, p in enumerate(prices):
            m = maxs[ix]
            if m and (m - p) > ans:
                ans = m - p
        return ans

s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))

