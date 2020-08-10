# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.range_sum = 0
        self.dfs(root, L, R)
        return self.range_sum

    def dfs(self, node, L, R):
        if node:
            if node.val >= L and node.val <= R:
                self.range_sum = self.range_sum + node.val
            self.dfs(node.left, L, R)
            self.dfs(node.right, L, R)

        

tree = TreeNode(10)
tree.left = TreeNode(5)
tree.right = TreeNode(15)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(7)
tree.right.right = TreeNode(18)

s = Solution()
print(s.rangeSumBST(tree, 7, 15))

tree2 = TreeNode(10)
tree2.left = TreeNode(5)
tree2.right = TreeNode(15)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(7)
tree2.right.left = TreeNode(13)
tree2.right.right = TreeNode(18)
tree2.left.left.left = TreeNode(1)
tree2.right.left.left = TreeNode(6)

s = Solution()
print(s.rangeSumBST(tree2, 6, 10))
