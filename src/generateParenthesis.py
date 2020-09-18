class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']

        if n == 1:
            return ['()']

        ans = []
        for ix in range(n):
            for l in self.generateParenthesis(ix):
                for r in self.generateParenthesis(n-ix-1):
                    ans.append('({}){}'.format(l, r))
        return ans

s = Solution()
print(s.generateParenthesis(4))