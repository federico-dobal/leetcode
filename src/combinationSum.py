class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        partial_target = [[target - e, [e]] for e in candidates]
        ans = [e[1] for e in partial_target if e[0] == 0]

        for t in partial_target:
            for n in candidates:
                delta = t[0] - n

                if delta == 0:
                    result = t[1]+[n]
                    result.sort()
                    if result not in ans:
                        ans.append(result)

                if delta > 0:
                    partial_target.append((delta, t[1]+[n]))

        return ans

s = Solution()
print(s.combinationSum([2,3,5], 7))