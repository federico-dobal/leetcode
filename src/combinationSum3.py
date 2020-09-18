class Solution(object):
    def getCombinations(self, k, S, ans):
        if k == 0:
            next_ans = []
            for e in ans:
                if e not in next_ans:
                    next_ans.append(e)

            return next_ans
        else:
            if not ans:
                return self.getCombinations(k - 1, S, [[n] for n in range(1,10) if n <= S])
            else:
                next_ans = []
                for e in range(1, 10):
                    next_ans.extend(self.getCombinations(k-1, S, [n + [e] for n in ans if e > n[-1] and sum(n + [e]) <= S]))

                return [e for e in next_ans if sum(e) == S]


    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return [x for x in self.getCombinations(k, n, []) if len(x)==k]

s = Solution()
print(s.combinationSum3(3, 7))