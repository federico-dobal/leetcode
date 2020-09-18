class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        max_len = 0
        N = len(s)
        for ix, c in enumerate(s):
            if (N-ix) < N:
                break

            max_start_ix, max_end_ix = ix, ix
            while max_end_ix < N and s[max_end_ix] not in s[max_start_ix:max_end_ix]:
                max_end_ix += 1

            if (max_end_ix-max_start_ix) > max_len:
                max_len = max_end_ix-max_start_ix

        return max_len

s = Solution()
print(s.lengthOfLongestSubstring(''))
print(s.lengthOfLongestSubstring('abcabcbb'))
print(s.lengthOfLongestSubstring('aaaaa'))
print(s.lengthOfLongestSubstring('pwwkew'))

