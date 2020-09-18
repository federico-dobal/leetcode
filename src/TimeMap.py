import sys
import bisect


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_dict = {}
        self.min_ts = sys.maxsize
        self.sorted_ts = []

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if self.time_dict.get(timestamp):
            self.time_dict.get(timestamp)[key] = value
        else:
            self.time_dict[timestamp] = {key: value}
            if timestamp not in self.sorted_ts:
                l, r = 0, len(self.sorted_ts)
                if r >= 0:
                    bisect.insort(self.sorted_ts, timestamp)
                else:
                    self.sorted_ts = [timestamp]

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if timestamp < self.sorted_ts[0]:
            return ""

        fail = True
        ix_ts = timestamp
        while fail and ix_ts > 0:
            try:
                ix_ts = self.sorted_ts.index(ix_ts)
            except ValueError:
                fail = True
                ix_ts -= 1
                continue
            fail = False

        while ix_ts >= 0:
            dict_ts = self.time_dict.get(self.sorted_ts[ix_ts])
            if dict_ts:
                v = dict_ts.get(key)
                if v:
                    return v
                else:
                    ix_ts -= 1
            else:
                ix_ts -= 1
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)