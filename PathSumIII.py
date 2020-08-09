# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.map_sum = {}
        count = 0
        self.dfs(root, None)
        print(self.map_sum.values())
        for pos_sum in self.map_sum.values():
            for s in pos_sum:
                if sum == s:
                    count = count + 1
        return count


    def dfs(self, node, parent):
        if node:
            if parent:
                self.map_sum[node] = []
                self.map_sum[node].append(node.val)
                for s in self.map_sum[parent]:
                    self.map_sum[node].append(s + node.val)
            else:
                self.map_sum[node] = [node.val]
            self.dfs(node.left, node)
            self.dfs(node.right, node)




        
tree2 = TreeNode(10)
tree2.left = TreeNode(5)
tree2.right = TreeNode(-3)
tree2.left.left = TreeNode(3)
tree2.left.right = TreeNode(2)
tree2.right.right = TreeNode(11)
tree2.left.left.left = TreeNode(3)
tree2.left.left.right = TreeNode(-2)
tree2.left.right.right = TreeNode(1)

s = Solution()
print(s.pathSum(tree2, 8))


tree3 = TreeNode(0)
tree3.left = TreeNode(1)
tree3.right = TreeNode(1)

s = Solution()
print(s.pathSum(tree3, 1))