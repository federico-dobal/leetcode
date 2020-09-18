from math import sqrt


class Solution(object):

    def getDelta(self, p1, p2):
        return sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))

    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        points = []
        for p in [p1, p2, p3, p4]:
            if p not in points:
                points.append(p)
        if len(points) < 4:
            return False

        for p in points:
            ps = [pa for pa in points if p != pa]
            deltas = [self.getDelta(p, pa) for pa in ps]
            deltas.sort()
            if deltas[0] != deltas[1]:
                return False
            else:
                h = deltas[0]
                for pa in ps:
                    if pow(h, 2) - (pow(p[0] - pa[0], 2) + pow(p[1] - pa[1], 2)) <= 0.00001:
                        continue
                return False

        return True



s = Solution()
print(s.validSquare([0,0],
[-1,0],
[1,0],
[0,1]
))

exit(0)
print(s.validSquare([1134,-2539],
                    [492,-1255],
                    [-792,-1897],
                    [-150,-3181]))
