from heapq import heapify, _siftup, _siftdown, heappop

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print (nums)
        h = [(-e, ix) for ix, e in enumerate(nums)]
        print(h)
        heapify(h)
        print(h)
        #print(heappop(h))
        print(h)
        ixs_retrieved = []
        ans = 0
        while h:
            (n, ix) = heappop(h)
            if ix + 1 in ixs_retrieved or ix - 1 in ixs_retrieved:
                continue

            if ix + 1 not in ixs_retrieved and ix - 1 not in ixs_retrieved:
                if 0<=ix-1<len(nums):
                    if 0<=ix+1<len(nums):
                        if (-n) > (nums[ix-1] + nums[ix+1]):
                            if ix not in ixs_retrieved:
                                ixs_retrieved.append(ix)
                                ans += -n
                    else:
                        if (-n) > (nums[ix-1]):
                            if ix not in ixs_retrieved:
                                ixs_retrieved.append(ix)
                                ans += -n
                else:
                    if 0<=ix+1<len(nums):
                        if (-n) > (nums[ix+1]):
                            if ix not in ixs_retrieved:
                                ixs_retrieved.append(ix)
                                ans += -n
                    else:
                        if ix not in ixs_retrieved:
                                ixs_retrieved.append(ix)
                                ans += -n

            if ix-1 not in ixs_retrieved:
                if (-n) > (nums[ix - 1]):
                    if ix not in ixs_retrieved:
                        ixs_retrieved.append(ix)
                        ans += -n
                    continue



            if ix+1 not in ixs_retrieved:
                if (-n) > (nums[ix + 1]):
                    if ix not in ixs_retrieved:
                        ixs_retrieved.append(ix)
                        ans += -n
                    continue


            ixs_retrieved.append(ix)
            ans += -n

        return ans

s = Solution()
print (s.rob([2,3,2]))
#print (s.rob([2,1,1,2]))
#print (s.rob([1,5,9,12]))