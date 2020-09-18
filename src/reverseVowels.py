class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = [c for c in s if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
        vi = len(vowels) - 1
        ans = ""
        for i, c in enumerate(s):
            if c in ['a', 'e', 'i', 'o', 'u']:
                ans += vowels[vi]
                vi -= 1
            else:
                ans += c
        return ans

s = Solution()
print(s.reverseVowels("hello"))


