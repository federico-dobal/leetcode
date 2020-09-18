class Solution(object):
    partial_result = {}

    def getFromCache(self, elems, k):
        if k not in self.partial_result.keys():
            return self.combineHelper(elems, k)
        else:
            result = self.partial_result.get(k)
            self.partial_result[k] = result
            return result

    def combineHelper(self, elems, k):
        if k == 0:
            return []

        if k == 1:
            return [[e] for e in elems]

        sub_results_1 = self.getFromCache(elems, middle)

        middle = k / 2
        sub_results_1 = self.getFromCache(elems, middle)

        if k % 2 == 0:
            sub_results_2 = self.getFromCache(elems, middle)
        else:
            sub_results_2 = self.getFromCache(elems, 1 + middle)

        ans = []
        for l in sub_results_1:
            for r in sub_results_2:
                if l == r:
                    continue
                result = l + r
                if result not in ans:
                    ans.append(result)
        return ans

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combineHelper(list(range(1, 1+n)), k)

s = Solution()
print(s.combine(4, 2))