class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        if not A:
            return 0
        N, M = len(A), len(A[0])
        r = 0
        while r < N:
            if A[r][0] == 0:
                A[r] = [1-i for i in A[r]]
            r += 1

        c = 1
        while c < M:
            print([A[i][c] for i in range(N)])
            ones_in_col = sum([A[i][c] for i in range(N)])
            if ones_in_col < (N//2)+1:
                i = 0
                while i < N:
                    A[i][c] = 1 - A[i][c]
                    i += 1
            c += 1

        ans = 0
        for r in A:
            i = M-1
            num = 0
            while i >= 0:
                num += r[M-i-1] * (1<<i)
                i -= 1

            ans += num
        return ans


s = Solution()
print(s.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))