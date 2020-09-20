# Definition for a binary tree node.
from heapq import heappush
from heapq import heappop
from heapq import heapify

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    

class Solution(object):
    def getElements(self, n):
        if not n:
            return []
        l = self.getElements(n.left)
        r = self.getElements(n.right)
        return [n.val] + l + r

    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        l1 = self.getElements(root1)
        l2 = self.getElements(root2)
        h = l1 + l2
        heapify(h)


        ans = []
        while h:
            ans.append(heappop(h))

        return ans




n22 = TreeNode(3, None, None)
n21 = TreeNode(0, None, None)

n12 = TreeNode(4, None, None)
n11 = TreeNode(1, None, None)

n2 = TreeNode(1, n21, n22)
n1 = TreeNode(2, n11, n12)
#n0 = TreeNode(5, n1, n2)

s = Solution()
s.getAllElements(n1, n2)