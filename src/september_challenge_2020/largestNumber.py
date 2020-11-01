class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        def comparator(a, b):
            ab = str(a) + str(b)
            ba = str(b) + str(a)
            return ((int(ba) > int(ab)) - (int(ba) < int(ab)))

        def myCompare(mycmp):

            # Convert a cmp= function into a key= function
            class K(object):
                def __init__(self, obj, *args):
                    self.obj = obj

                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0

                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0

                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0

                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0

                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0

                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0

            return K

        numbers = [[]] * 10
        ans = ""
        for n in nums:
            first_digit = int(str(n)[0])
            numbers[first_digit] = numbers[first_digit] + [n]

        for i in range(9, 0, -1):
            if not numbers[i]:
                continue

            numbers[i].sort(key=myCompare(comparator))

            ans += ''.join([str(x) for x in numbers[i]])

        if len(ans)>0:
            ans += ''.join(map(str, numbers[0]))
        else:
            ans = '0'
        return ans




s = Solution()
print(s.largestNumber([10,2]), "210")
print(s.largestNumber([121,12]), "12121")
print(s.largestNumber([3,30,34,5,9]), "9534330")
print(s.largestNumber([1,2,3,4,5,6,7,8,9,0]), "9876543210")
print(s.largestNumber([1,2,4,8,16,32,64,128,256,512]), "8645124322562161281")
print(s.largestNumber([1,0,0]), "100")


