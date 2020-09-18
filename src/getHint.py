class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        letters_to_pos = {}
        new_guess = ""
        bull, cow = 0, 0
        for ix, c in enumerate(secret):
            if guess[ix] == c:
                bull += 1
                continue
            new_guess = new_guess + guess[ix]
            pos = letters_to_pos.get(c)
            if not pos:
                letters_to_pos[c] = 1
            else:
                letters_to_pos[c] += 1

        for ix, g in enumerate(new_guess):
            pos = letters_to_pos.get(g)
            if pos:
                cow += 1
                letters_to_pos[g] -= 1

        return "{}A{}B".format(bull, cow)


s = Solution()
print(s.getHint("1123", "0111"))
"1A1B"