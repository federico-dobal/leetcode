from heapq import heappush
from heapq import heappop
from heapq import heapify

class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.nb_items = 0
        self.size = N
        self.intervals = []
        self.ix_to_intervals = {}
        #self.intervals.push([0,N-1])

    def seat(self):
        """
        :rtype: int
        """


        if self.nb_items == 0:
            heappush(self.intervals, (0, [0, 0]))
            heappush(self.intervals, (-(self.size-1), [1, self.size-1]))
            self.ix_to_intervals[0] = [[0, 0], [0, self.size-1]]
            self.nb_items += 1
            return 0

        self.nb_items += 1
        longest_interval = heappop(self.intervals)[1]

        if longest_interval[1] == self.size-1:
            heappush(self.intervals, (-(longest_interval[1]-1-longest_interval[0]), [longest_interval[0], longest_interval[1]-1]))
            heappush(self.intervals, (0, [longest_interval[1], longest_interval[1]]))
            self.ix_to_intervals[0] = [[longest_interval[0], longest_interval[1]-1], [longest_interval[1], longest_interval[1]]]
            return longest_interval[1]

        split_interval_position = (longest_interval[0]+longest_interval[1]) // 2

        heappush(self.intervals, (-(split_interval_position - longest_interval[0]), [longest_interval[0], split_interval_position]))
        heappush(self.intervals, (-(longest_interval[1] - split_interval_position - 1), [split_interval_position+1, longest_interval[1]]))
        self.ix_to_intervals[split_interval_position] = [[longest_interval[0], split_interval_position],  [split_interval_position+1, longest_interval[1]]]

        return split_interval_position


    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        merge_ints = self.ix_to_intervals[p]

        l = self.intervals.index(merge_ints[0])
        self.intervals[l] = self.intervals[-1]
        heapify(self.intervals[:-2])

        r = self.intervals.index(merge_ints[1])
        self.intervals[l] = self.intervals[-1]
        heapify(self.intervals[:-2])

        heappush(self.intervals, (-(r[1]-l[0]), [l[0], r[1]]))

        self.nb_items -= 1


er = ExamRoom(10)
print(er.seat())
print(er.seat())
print(er.seat())
print(er.seat())
print(er.leave(4))
print(er.seat())