class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans = 0
        for ix, n in enumerate(timeSeries):
            if ix ==0:
                delta = duration + 1
            else:
                delta = n - timeSeries[ix-1]

            if delta >= duration:
                ans += duration
            else:
                ans += delta

        return ans


s = Solution()
print(s.findPoisonedDuration([1, 4], 2), 4)
print(s.findPoisonedDuration([1, 2], 2), 3)
print(s.findPoisonedDuration([1, 2, 3], 1), 3)
print(s.findPoisonedDuration([1, 2, 3, 4, 5], 5), 9)