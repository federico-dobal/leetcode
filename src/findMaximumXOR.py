class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = None
        for n in nums:
            for m in nums:
                if not ans or (n ^ m) > ans:
                    ans = n ^ m

        return ans

s = Solution()
print(s.findMaximumXOR([3, 10, 5, 25, 2, 8]))