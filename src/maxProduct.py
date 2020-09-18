import functools

class Solution(object):

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = None
        for ix, v in enumerate(nums):
            partial = 1
            for last in range(ix, len(nums)):
                partial = partial * nums[last]

                if ans == None or partial > ans:
                    ans = partial

            if ans == None or partial > ans:
                ans = partial

        return ans if ans else 0

s = Solution()
print(s.maxProduct([-3,0,1,-2]))