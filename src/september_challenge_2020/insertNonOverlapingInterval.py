class Solution(object):

    def isThereOverlap(self, newInterval, current):
        s, e = newInterval[0], newInterval[1]
        sc, ec = current[0], current[1]
        return (s >= sc and e <= ec) or \
               (sc >= s and ec <= e) or \
               (s >= sc and s<=ec and e > ec) or \
               (s < sc and e>=sc and e <= ec)

    def firstOverlaping(self, intervals, newInterval, l, r):
        m = (r-l)//2
        if l<r:
            if self.isThereOverlap(newInterval, intervals[m]):
                if newInterval[0] <= intervals[m][0] and newInterval[1] >= intervals[m][1]:
                    return self.firstOverlaping(intervals, newInterval, l, m)
                else:
                    return m
            elif intervals[m][1]<newInterval[0] and newInterval[1]<intervals[m+1][0]:
                return m
            else:
                if intervals[m][1] < newInterval[0]:
                    return self.firstOverlaping(intervals, newInterval, m+1, r)
                else:
                    return self.firstOverlaping(intervals, newInterval, l, m)
        else:
            return None

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        s, e = newInterval[0], newInterval[1]
        overlaps = []
        pos, pos_o = None, None

        fo = self.firstOverlaping(intervals, newInterval, 0, len(intervals))
        if fo is not None:
            if intervals[fo][1]<newInterval[0] and newInterval[1]<intervals[fo+1][0]:
                return intervals[:fo+1] + [newInterval] + intervals[fo+1:]
            else:
                i = fo
                while i<len(intervals) and self.isThereOverlap(newInterval, intervals[i]):
                    if intervals[i][0] < s:
                        s = intervals[i][0]
                    if intervals[i][1] > e:
                        e = intervals[i][1]
                    i += 1
                return intervals[:fo] + [[s,e]] + intervals[i:]
        else:
            return intervals

        return

        print(fo)
        for ix, c in enumerate(intervals):
            sc, ec = c[0], c[1]
            # Overlaps
            if (s >= sc and e <= ec) or (sc >= s and ec <= e) or (s >= sc and s<=ec and e > ec) or (s < sc and e>=sc and e <= ec):
                overlaps.append(c)
            if s<sc:
                if not pos_o:
                    pos_o = ix

            else:
                if not pos and ec<s:
                    pos = ix

        if overlaps:
            #s, e = overlaps[0][0], overlaps[0][1]
            #intervals.remove(overlaps[0])
            for c in overlaps:
                #intervals.remove(c)
                if c[0] < s:
                    s = c[0]
                if c[1] > e:
                    e = c[1]
            ans = []
            ins = False
            for c in intervals:
                if c in overlaps:
                    if not ins:
                        ans.append([s, e])
                        ins = True
                else:
                    ans.append(c)
            return ans

        else:
            return intervals[:pos_o] + [newInterval] + intervals[pos_o:]


s = Solution()
#print(s.insert([[1,3],[6,9]], [2,5]))
print(s.insert([[1,2],[1,3],[1,4],[1,5],[1,6]], [1,7]))
#print(s.insert([[1,5]], [6,8]))
#print(s.insert([], [5,7]))
#print(s.insert([[1,5]], [0,0]))
#print(s.insert([[2,6],[7,9]], [15,18]))
#print(s.insert([[4,6],[7,9]], [1,2]))


print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(s.insert([[0,10],[14,14],[15,20]], [11,11]))

