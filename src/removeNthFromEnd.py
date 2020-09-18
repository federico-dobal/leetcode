# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

     def printList(self):
        cur = self
        while True:
            if not cur:
                break

            print(cur.val, ' --> ')
            cur = cur.next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if n == 0:
            return head

        if not head.next:
            if n == 1:
                return None
            else:
                return head

        end = head
        for _ in range(n):
            if not end.next:
                return head.next
            end = end.next

        start = head
        while end.next !=None:
            start = start.next
            end = end.next
        start.next = start.next.next
        return head





n5 = ListNode(5, None)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

s = Solution()
print('==========')
n1.printList()
print('==========')
s.removeNthFromEnd(n1, 5).printList()


