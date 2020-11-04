'''
Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            new_head = ListNode(head.val, None)
            cursor = head.next
            while cursor:
                start = new_head
                while start.next and start.next.val < cursor.val:
                    start = start.next

                if start != new_head:
                    n = start.next
                    start.next = ListNode(cursor.val, n)
                else:
                    if cursor.val < new_head.val:
                        h = ListNode(cursor.val, ListNode(new_head.val, new_head.next))
                    else:
                        h = ListNode(new_head.val, ListNode(cursor.val, new_head.next))
                    new_head = h
                cursor = cursor.next


        return new_head

n13 = ListNode(3, None)
n12 = ListNode(1, n13)
n11 = ListNode(5, None)
n1 = ListNode(-1, n11)

s = Solution()
print(s.insertionSortList(n1))
