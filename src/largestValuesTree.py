# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution(object):
    def __init__(self):
        self.max_level = {}

    def findLargest(self, root, level):
        if not root:
            return
        else:
            currentMax = self.max_level.get(level)
            if currentMax != None:
                if root.val > currentMax:
                    self.max_level[level] = root.val
            else:
                self.max_level[level] = root.val

            if root.left:
                self.findLargest(root.left, level + 1)

            if root.right:
                self.findLargest(root.right, level + 1)

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.findLargest(root, 0)
        return self.max_level.values()


n22 = TreeNode(9, None, None)
n22 = TreeNode(9, None, None)

n12 = TreeNode(3, None, None)
n11 = TreeNode(5, None, None)

n2 = TreeNode(-37, None, None)
n1 = TreeNode(0, None, None)
n0 = TreeNode(-40, n1, n2)

s = Solution()
print(s.largestValues(n0))