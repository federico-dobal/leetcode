class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return []

        last = {}
        for ix, c in enumerate(S):
            last[c] = ix

        ans = []
        start, end = 0, last.get(S[0])

        print(last)
        while start < len(S):
            max_last = max([last.get(x) for x in S[start:end+1]])
            if max_last <= end:
                ans.append(end-start+1)
                start = end + 1
                if start >= len(S):
                    return ans
                end = last.get(S[start])
            else:
                end = max_last


        return ans

s = Solution()
print(s.partitionLabels("abaccbdeffed"))
print(s.partitionLabels("abaccbdeffeda"))
print(s.partitionLabels(""))