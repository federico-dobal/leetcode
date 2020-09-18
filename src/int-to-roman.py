class Solution(object):

    map_numbers = {1: 'I',
                   5: 'V',
                   10: 'X',
                   50: 'L',
                   100: 'C',
                   500: 'D',
                   1000: 'M'
                   }

    map_next_numbers = {1: 5,
                   5: 10,
                   10: 50,
                   50: 100,
                   100: 500,
                   500: 1000
                   }

    def calculateRoman(self, times, which):

        roman_letter = self.map_numbers.get(which, '')
        ans = ''
        partial_ans = ''

        which_n = times * which

        if which_n == 4:
            return 'IV'

        if which_n == 9:
            return 'IX'

        if which_n == 40:
            return 'XL'

        if which_n == 90:
            return 'XC'

        if which_n == 400:
            return 'CD'

        if which_n == 900:
            return 'CM'

        if which_n in self.map_numbers.keys():
            return self.map_numbers.get(which_n)
        else:
            acc = 0
            for _ in range(times):
                partial_ans += self.map_numbers.get(which, '')
                acc += which
                if acc != which and acc in self.map_numbers.keys():
                    ans += self.map_numbers.get(acc)
                    partial_ans = ''
                    acc = 0
            ans += partial_ans

        print(times, which, times * which, ans)
        return ans

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        pos = 10 ** (len(str(num)) - 1)
        ans = ''
        for n in str(num):
            ans += self.calculateRoman(int(n), int(pos))
            pos = pos / 10
        return ans




s = Solution()
print(s.intToRoman(58))