import itertools

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        T = ["{}{}:{}{}".format(x[0], x[1], x[2], x[3]) for x in list(itertools.permutations(A))]
        T = list(filter(lambda x: 0 <= int(x[:2]) < 24 and 0 <= int(x[3:]) < 60, T))
        if not T:
            return ""
        m = max([(int(t[:2]), t) for t in T])

        return m[1]

s = Solution()
#print(s.largestTimeFromDigits([1,2,3,4]))
#print(s.largestTimeFromDigits([5,5,5,5]))
#print(s.largestTimeFromDigits([2,2,3,4]))
#print(s.largestTimeFromDigits([9,9,9,9]))
print(s.largestTimeFromDigits([2,0,6,6]))


