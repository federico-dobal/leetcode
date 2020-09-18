class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""



        c = 0
        ans = ""
        while c < len(s):

            #if s[c] == s[c+1]:
            # palindrome candidate has EVEN chars
            delta = 0
            while c-delta >= 0 and c+delta+1 < len(s) and s[c-delta] == s[c+delta+1]:
                delta += 1

            if 2*delta > len(ans):
                ans = s[c-delta+1:c+delta+1]
            #else:
            # palindrome candidate has ODD chars
            delta = 1
            while c-delta >= 0 and c+delta < len(s) and s[c-delta] == s[c+delta]:
                delta += 1
            if 1 + 2*(delta-1) > len(ans):
                ans = s[c-delta+1:c+delta]

            c += 1

        return ans

s = Solution()
print(s.longestPalindrome("ccc"))
print(s.longestPalindrome("bb"))
