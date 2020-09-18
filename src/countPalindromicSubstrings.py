class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0

        c = 0
        ans = []
        while c < len(s):

            ans.append(s[c])

            # palindrome candidate has EVEN chars
            delta = 0
            while c-delta >= 0 and c+delta+1 < len(s) and s[c-delta] == s[c+delta+1]:
                delta += 1

                if s[c-delta+1:c+delta+1] and len(s[c-delta+1:c+delta+1])>1:
                    ans.append(s[c-delta+1:c+delta+1])

            # palindrome candidate has ODD chars
            delta = 1
            while c-delta >= 0 and c+delta < len(s) and s[c-delta] == s[c+delta]:
                delta += 1

                if s[c-delta+1:c+delta] and len(s[c-delta+1:c+delta])>1:
                    ans.append(s[c-delta+1:c+delta])


            c += 1

        print(ans)
        return len(ans)


s = Solution()
print(s.countSubstrings("abc"))
print(s.countSubstrings("ccc"))
print(s.countSubstrings("abcdedcba"))
