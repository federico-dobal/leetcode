class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        ans = 0

        max_reached = intervals[0][1]
        for ix in range(1, len(intervals)):
            start = intervals[ix][0]
            if start < max_reached:
                ans += 1
            else:
                max_reached = intervals[ix][1]

        return ans

s = Solution()
print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(s.eraseOverlapIntervals([[1,2],[2,3]]))