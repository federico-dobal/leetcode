class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l, r = 0, len(nums) - 1
        if l == r:
            return nums[l]
        else:
            while l < r:
                if r-l < 2:
                    return min(nums[l], nums[r])
                m = l + (r-l) // 2
                if nums[m-1] > nums[m] and nums[m+1] > nums[m]:
                    l = m
                    break
                else:
                    if nums[m] > nums[r]:
                        l = m + 1
                    else:
                        r = m
            return nums[l]


s = Solution()
#print(s.findMin([3,4,5,1,2]))
#print(s.findMin([4,5,6,7,0,1,2]))
print(s.findMin([3,1,2]))
#print(s.findMin([2,3,4,5,1]))
