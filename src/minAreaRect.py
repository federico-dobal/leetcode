def isSquare(p, q):
    return p[0] == q[0] or p[1] == q[1]


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 4:
            return 0

        min_area = 40000 * 40000
        for ix1 in range(len(points)):
            for ix2 in range(ix1 + 1, len(points)):
                for ix3 in range(ix2 + 1, len(points)):
                    for ix4 in range(ix3 + 1, len(points)):
                        if (isSquare(points[ix1], points[ix2]) or isSquare(points[ix1], points[ix3]) or isSquare(points[ix1], points[ix4])) and \
                                (isSquare(points[ix2], points[ix3]) or isSquare(points[ix2], points[ix4])) and \
                                isSquare(points[ix3], points[ix4]):

                            vs = [points[ix1], points[ix2], points[ix3], points[ix4]]
                            xs = [x[0] for x in vs]
                            ys = [x[1] for x in vs]
                            area = (max(xs) - min(xs)) * (max(ys) - min(ys))
                            if area < min_area:
                                min_area = area

        return min_area

s = Solution()
print(s.minAreaRect([[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]]))
