class Solution(object):
    def removeLeadingZeroes(self, v):
        i1 = len(v) - 1
        while i1 >=0:
            if v[i1] == 0:
                i1 -=1
            else:
                return v[:i1+1]
        return v

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = self.removeLeadingZeroes(list(map(int, version1.split('.'))))
        v2 = self.removeLeadingZeroes(list(map(int, version2.split('.'))))

        print (v1)
        print(v2)
        i1, i2 = 0, 0
        while i1 < len(v1) and i2 < len(v2):
            if v1[i1] == v2[i2]:
                i1, i2 = i1 + 1, i2 + 1
            else:
                return -1 if v1[i1] < v2[i2] else 1

        if i1 == len(v1) and i2 == len(v2):
            return 0
        else:
                    return -1 if len(v1) < len(v2) else 1



s = Solution()
print(s.compareVersion("0.1", "0.0.1"))