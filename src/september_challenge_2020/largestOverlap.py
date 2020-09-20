class Solution(object):
    def getOnes(self, l):
        ones = []
        for ix, i in enumerate(l):
            for jx, j in enumerate(l[ix]):
                if l[ix][jx] == 1:
                    ones.append((ix, jx))
        return ones

    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        onesA= self.getOnes(A)
        onesB = self.getOnes(B)
        print(onesA)
        print(onesB)
        count = {}
        ans = 0
        for pa in onesA:
            for pb in onesB:
                p = (pb[0]-pa[0], pb[1]-pa[1])
                if count.get(p):
                    count[p] += 1
                else:
                    count[p] = 1
                if count[p] > ans:
                    ans = count[p]

        return ans


A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
B = [[0,0,0],
    [0,1,1],
    [0,0,1]]

s = Solution()
print(s.largestOverlap([[1,1,1],[1,1,1],[1,1,1]],
[[1,1,1],[1,1,1],[1,1,1]]))