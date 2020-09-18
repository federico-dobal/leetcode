import re

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        regexp = "\s(\w+)$"
        match = re.search(regexp, s.strip())
        if match:
            return len(match.group()) - 1

        else:
            return len(s)


s = Solution()
print (s.lengthOfLastWord("HelloWorld"))