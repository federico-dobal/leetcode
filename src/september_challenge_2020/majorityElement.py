"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""

import math


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        ans = []
        L = math.floor(len(nums)/3)
        for n in nums:
            if n in ans:
                continue
            c = d.get(n, 0)
            if not c:
                if 1 > L:
                    ans.append(n)
                d[n] = 1
            else:
                v = c + 1
                if v > L:
                    ans.append(n)
                d[n] = v
        return ans

s = Solution()
print (s.majorityElement([3,2,3]), [3])
print (s.majorityElement([1,1,1,3,3,2,2,2]), [1,2])
print (s.majorityElement([1]), [1])
print (s.majorityElement([]), [])
print (s.majorityElement([1,1,1,1,1,1,1]), [1])




