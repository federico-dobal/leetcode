class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anags = {}
        for s in strs:
            ssort = list(s)
            ssort.sort()
            ssort = str(ssort)
            if anags.get(ssort):
                anags.get(ssort).append(s)
            else:
                anags[ssort] = [s]

        return [v for v in anags.values()]

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))