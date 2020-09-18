import requests

class Solution(object):

    def findElemsSum(self, nums, S):
        ans = []
        N = len(nums)
        if N<2 or nums[N-1] + nums[N-2] < S:
            return []
        for ix, n in enumerate(nums):
            l, r = ix + 1, len(nums) - 1
            while l < r:
                mid = l + (r - l) // 2
                if S > n + nums[mid]:
                    l = mid+1
                    continue
                if S < n + nums[mid]:
                    r = mid
                    continue
                if S == n + nums[mid]:
                    if [n, nums[mid]] not in ans:
                        ans.append([n, nums[mid]])
                    break
            mid = l + (r - l) // 2
            if S == n + nums[mid]:
                if [n, nums[mid]] not in ans:
                    ans.append([n, nums[mid]])

        return ans

    def search(self, pos, neg, order):
        ans = []
        for n in neg:
            for p in self.findElemsSum(pos, -n):
                if p not in ans:
                    if order:
                        res = [p[0], p[1], n]
                    else:
                        res = [n, p[0], p[1]]

                    if res not in ans:
                        ans.append(res)

        return ans

    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums.sort()

        pos = [n for n in nums if n >= 0]
        neg = [n for n in nums if n < 0]

        zeros = [n for n in nums if n == 0]
        ans = []
        if len(zeros) >= 3:
            ans.append([0, 0, 0])

        return self.search(pos, neg, False) + self.search(neg, pos, True) + ans
        #return self.search(neg, pos, True)


s = Solution()
url_tc = 'https://leetcode.com/submissions/detail/382595932/testcase/'
tc = requests.get(url_tc)
print(tc.status_code)
print(tc.text)
#print(s.threeSum([-1,0,1]))
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
# print(s.threeSum([-1, 0, 1, 2, -1, -4]))
#print(s.threeSum([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]))
