class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type N: int
        :rtype: int
        """

        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        ans = 1

        print (points)
        max_reached = points[0][1]
        for ix in range(1, len(points)):
            if max_reached < points[ix][0]:
                max_reached = points[ix][1]
                ans += 1




        return ans

s = Solution()
print(s.findMinArrowShots([[10,16], [2,8], [1,6], [7,12]]))