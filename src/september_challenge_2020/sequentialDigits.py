"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
"""
class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        N = len(str(low))
        start = low // 10**(N-1) % 10
        while True:
            if start-1 > 9-N:
                start = 1
                N += 1
            current = start
            j = 1
            while j < N:
                current = current * 10 + (start + j)
                j += 1
            if current >= low:
                break
            else:
                start += 1

        ans = []
        while current <= high:
            ans.append(current)
            s = current // 10 ** (N - 1) % 10 + 1
            if s > 9 - N + 1:
                s = 1
                N += 1
            current = s
            j = 1
            while j<N:
                current = current * 10 + (s + j)
                j += 1
        return ans

s = Solution()
print(s.sequentialDigits(100, 300))
print(s.sequentialDigits(1000, 13000))
print(s.sequentialDigits(58 , 155))
print(s.sequentialDigits(8511, 23553))
print(s.sequentialDigits(744, 1928))
