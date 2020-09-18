class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        N, M = len(matrix), min([len(r) for r in matrix])

        if N == M and N == 1:
            return matrix[0]

        up = True
        r, c = 0, 0
        ans = []
        while r < N and c < M:
            ans.append(matrix[r][c])

            if up:
                if r == 0 or c == M-1:
                    if c == M-1:
                        r = r + 1
                        up = False
                        continue
                    c = c + 1
                    up = False
                    continue
                r, c = r - 1, c + 1
            else:
                if c == 0 or r == N-1:
                    if r == N-1:
                        c = c + 1
                        up = True
                        continue
                    r = r + 1
                    up = True
                    continue
                r, c = r + 1, c - 1

        return ans

s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
