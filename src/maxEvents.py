import functools
import sys

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        N = pow(10, 5)

        # min_start, max_end = min([e[0] for e in events]), max([e[1] for e in events])
        used = [False for _ in range(N)]

        ans = 0
        events.sort(key=functools.cmp_to_key(lambda x, y: x[0] - y[0] if x[1] == y[1] else x[1] - y[1]), reverse=True)
        # events.sort(key=lambda x: x[0], reverse=True)
        last = sys.maxsize
        last_end, last_start = None, None
        while events:
            ev = events.pop()
            s, e = ev[0], ev[1]
            if (last_start and s == last_start) or (last_end and e == last_end):
                ix = last-1
            else:
                ix = s - 1

            while ix < e:
                # delta_ix = ix - min_start
                if ix >= N:
                    break

                if not used[ix]:
                    used[ix] = True
                    ans += 1
                    last = ix + 1
                    last_start, last_end = s, e
                    break
                else:
                    ix += 1

        return ans

s = Solution()
e = [[1,i] for i in range(1, 11)]
#e = [[1,4],[4,4],[2,2],[3,4],[1,1]]
#e = [[25,26],[19,19],[9,13],[16,17],[17,18],[20,21],[22,25],[11,12],[19,23],[7,9],[1,1],[21,23],[14,14],[4,7],[16,16],[24,28],[16,18],[4,5],[18,20],[16,16],[25,26]]
print(e)

print(s.maxEvents(e))

exit(0)
for e in [[[1,2],[1,2],[3,3],[1,5],[1,5]],
          [[1,2],[2,3],[3,4]],
          [[1,2],[2,3],[3,4],[1,2]],
          [[1,4],[4,4],[2,2],[3,4],[1,1]],
          [[1,100000]],
          [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]]:
    print(s.maxEvents(e))