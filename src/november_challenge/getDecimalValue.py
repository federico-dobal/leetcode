
'''
  Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        position = 0
        current = head
        res = 0
        length = 0
        while current.next:
            length += 1
            current = current.next

        current = head
        while current.next:
            res += current.val * pow(2, length - position)
            position += 1
            current = current.next
        res += current.val * pow(2, length - position)
        return res

n12 = ListNode(1, None)
n11 = ListNode(0, n12)
n1 = ListNode(1, n11)

s = Solution()
print(s.getDecimalValue(n1))