# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def sumRootToLeafAns(self, root):
        if not root:
            return []

        value = root.val
        partial_ans_l, partial_ans_r = [], []

        if root.left == None and root.right == None:
            return [[value]]

        if not root.left == None:
            partial_ans_l = [[value]+ x for x in self.sumRootToLeafAns(root.left)]

        if not root.right == None:
            partial_ans_r = [[value]+ x for x in self.sumRootToLeafAns(root.right)]

        return partial_ans_l + partial_ans_r

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = self.sumRootToLeafAns(root)
        print(ans)
        return sum([int("".join(map(str,x)), 2) for x in ans])


n22 = TreeNode(1, None, None)
n21 = TreeNode(0, None, None)

n12 = TreeNode(1, None, None)
n11 = TreeNode(0, None, None)

n2 = TreeNode(1, n21, n22)
n1 = TreeNode(0, n11, n12)
n0 = TreeNode(1, n1, n2)

s = Solution()
print(s.sumRootToLeaf(n0))