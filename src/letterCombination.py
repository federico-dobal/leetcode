class Solution(object):
    phone = {2: ['a', 'b', 'c'],
             3: ['d', 'e', 'f'],
             4: ['g', 'h', 'i'],
             5: ['j', 'k', 'l'],
             6: ['m', 'n', 'o'],
             7: ['p', 'q', 'r', 's'],
             8: ['t', 'u', 'v'],
             9: ['w', 'x', 'y', 'z']
             }
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        else:
            print(digits[1:])
            print (self.phone.get(int(digits[0])))
            sub_solution = self.letterCombinations(digits[1:])

            if len(sub_solution) == 0:
                return self.phone.get(int(digits[0]))
            else:
                ans = []
                for c in list(self.phone.get(int(digits[0]))):
                     ans += [c + l for l in sub_solution]

                return ans

s = Solution()
print(s.letterCombinations('23'))