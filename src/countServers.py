class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            ones = sum([x for x in grid[i] if x == 1])
            if ones > 1:
                ans += ones

        for j in range(m):
            s = []
            for i in range(n):
                s.append(grid[i][j])
            ones = sum([x for x in s if x == 1])
            if ones > 1:
                ans += ones

        return ans

s = Solution()
print(s.countServers([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))