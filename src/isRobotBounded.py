class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        pos_e, d_e = (0, 0), 'N'
        for i in instructions:
            if i == 'G':
                if d_e == 'N':
                    pos_e = (pos_e[0], pos_e[1]+1)
                    continue
                if d_e == 'L':
                    pos_e = (pos_e[0]-1, pos_e[1])
                    continue

                if d_e == 'R':
                    pos_e = (pos_e[0]+1, pos_e[1])
                    continue
                if d_e == 'S':
                    pos_e = (pos_e[0], pos_e[1]-1)
                    continue
            if i == 'L':
                if d_e == 'N':
                    d_e = 'L'
                    continue
                if d_e == 'L':
                    d_e = 'S'
                    continue
                if d_e == 'R':
                    d_e = 'N'
                    continue
                if d_e == 'S':
                    d_e = 'R'
                    continue
            if i == 'R':
                if d_e == 'N':
                    d_e = 'R'
                    continue
                if d_e == 'L':
                    d_e = 'N'
                    continue
                if d_e == 'R':
                    d_e = 'S'
                    continue
                if d_e == 'S':
                    d_e = 'L'
                    continue
        return 'N' != d_e or (0, 0) == pos_e

s = Solution()
print(s.isRobotBounded("GGLLGG"))