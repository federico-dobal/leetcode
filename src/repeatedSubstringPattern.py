class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for n in range(1,len(s)//2+1):
            e = [s[i:i + n] for i in range(0, len(s), n)]
            v = e[0]
            if len(e) == len(list(filter(lambda x: x == v, e))):
                return True
        return False




s = Solution()
print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("aacbaacb"))
print(s.repeatedSubstringPattern("aba"))