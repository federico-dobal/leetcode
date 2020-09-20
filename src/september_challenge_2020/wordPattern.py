class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        S = str.split()
        l_to_w = {}
        values = []
        if len(S) != len(pattern):
            return False

        for ix, c in enumerate(pattern):
            w = l_to_w.get(c)
            if w:
                if w != S[ix]:
                    return False
            else:
                if S[ix] in values:
                    return False
                else:
                    values.append(S[ix])
                    l_to_w[c] = S[ix]
        return True


s = Solution()
#print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog dog dog dog"))


