class Solution(object):

    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        if not trips:
            return True

        numbers = {}

        for t in trips:
            c = t[0]
            for i in range(t[1], t[2]):
                current_capacity = numbers.get(i)

                if not current_capacity:
                    numbers[i] = c
                else:
                    numbers[i] += c

                if numbers[i] > capacity:
                    return False

        return True

s = Solution()
print(s.carPooling([[2,1,5],[3,3,7]], 4), False)
print(s.carPooling([[2,1,5],[3,3,7]], 5), True)
print(s.carPooling([[2,1,5],[3,5,7]], 3), True)
print(s.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11), True)
print(s.carPooling([[3,2,7],[12,7,9],[8,3,9]], 11), False)
print(s.carPooling([[12,7,9]], 11), False)
print(s.carPooling([], 11), True)