import sys

class Solution(object):
    def smallestRangeIIRec(self, A, K, ix, partial_min, partial_max):
        if ix == len(A):
            return partial_max - partial_min
        else:

            min_plus, max_plus = None, None
            if A[ix] + K < partial_min:
                min_plus = A[ix] + K

            if A[ix] + K > partial_max:
                max_plus = A[ix] + K

            plus_res = self.smallestRangeIIRec([a + K if i == ix else a for i, a in enumerate(A)], K, ix + 1,
                                               min_plus if min_plus != None else partial_min,
                                               max_plus if max_plus != None else partial_max)

            min_plus, max_plus = None, None
            if A[ix] - K < partial_min:
                min_plus = A[ix] - K

            if A[ix] - K > partial_max:
                max_plus = A[ix] - K


            less_res = self.smallestRangeIIRec([a - K if i == ix else a for i, a in enumerate(A)], K, ix + 1,
                                               min_plus if min_plus != None else partial_min,
                                               max_plus if max_plus != None else partial_max)
            if plus_res < less_res:
                return plus_res
            else:
                return less_res

    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return self.smallestRangeIIRec(A, K, 0, sys.maxsize, -sys.maxsize)


s = Solution()

#print(s.smallestRangeII([1], 0))
#print(s.smallestRangeII([0,10], 2))
print(s.smallestRangeII([1,3,6], 3))
