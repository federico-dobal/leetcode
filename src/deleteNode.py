# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def printNode(self):
        if self:
            print(self.val)
        if self.left:
            self.left.printNode()

        if self.right:
            self.right.printNode()


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root

        if root.val == key:
            if not root.left:
                return root.right

            if not root.right:
                return root.left

            c = root.right
            while c.left:
                c = c.left
            root.val = c.val
            root.right = self.deleteNode(root.right, c.val)
            return root


n22 = TreeNode(9, None, None)
n21 = None

n12 = TreeNode(4, None, None)
n11 = TreeNode(2, None, None)

n2 = TreeNode(6, n21, n22)
n1 = TreeNode(3, n11, n12)
n0 = TreeNode(5, n1, n2)

s = Solution()
n0.printNode()
print("================")
r = s.deleteNode(n0, 3)
r.printNode()
