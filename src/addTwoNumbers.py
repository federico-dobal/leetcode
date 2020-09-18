
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def number(self, n):
        ans = ""
        c = n
        while c:
            ans += str(c.val)
            c = c.next
        return int(ans)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = ""
        c = l1
        while c:
            n1 += str(c.val)
            c = c.next
        print(self.number(l1))
        print(self.number(l2))
        ansN = str(self.number(l1) + self.number(l2))
        ans = None
        for d in range(len(ansN)):
            ans = ListNode(ansN[len(ansN) - d -1], ans)
        print(self.number(ans))
        return ans



n13 = ListNode(3, None)
n12 = ListNode(4, n13)
n11 = ListNode(2, n12)
n1 = ListNode(7, n11)


n22 = ListNode(4, None)
n21 = ListNode(6, n22)
n2 = ListNode(5, n21)

S = Solution()
S.addTwoNumbers(n1, n2)
