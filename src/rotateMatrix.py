class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for o in range(N//2):
            for i in range(0, N-2-o):
                print(matrix[o][o + i])
                a, b, c, d = matrix[o][o+i], matrix[o+i][N-o-1], matrix[N-o-1][N-1-o-i], matrix[N-o-1-i][o]
                matrix[o][o+i] = d
                matrix[o+i][N-o-1] = a
                matrix[N-o-1][N-1-o-i] = b
                matrix[N-o-1-i][o] = c

        return None

s = Solution()
M = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s.rotate(M)
print(M)