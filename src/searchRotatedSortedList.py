class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        if l == r:
            return l
        else:
            while l < r:
                if r-l < 2:
                    if nums[l] < nums[r]:
                        return l
                    else:
                        return r
                m = l + (r-l) // 2
                if nums[m-1] > nums[m] and nums[m+1] > nums[m]:
                    l = m
                    break
                else:
                    if nums[m] > nums[r]:
                        l = m + 1
                    else:
                        r = m
            return l

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        M = self.findMin(nums)
        if target>=nums[M] and target<=nums[len(nums)-1]:
            nums = nums[M:]
        else:
            nums = nums[:M+1]
            M = 0

        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                if target == nums[l]:
                    return l+M
                else:
                    return -1
            m = l + (r - l) // 2
            if target==nums[m]:
                return m + M
            else:
                if target < nums[m]:
                    r = m
                else:
                    l = m + 1
        if l>r:
            return -1
        return l+M

s = Solution()
print(s.search([3,1], 3))
exit(0)
print(s.search([4,5,6,7,0,1,2], 0))
#print(s.search([4,5,6,7,0,1,2], 1))
#print(s.search([4,5,6,7,0,1,2], 2))
#print(s.search([4,5,6,7,0,1,2], 4))
#print(s.search([4,5,6,7,0,1,2], 9))
print(s.search([1], 0))
print(s.search([], 0))
