# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        res = self.dfs(cloned, target)
        return res

    def dfs(self, node, target):
        if node:
            isSame = self.isSameTree(node,target)
            if isSame:
                return node
            res = self.dfs(node.left, target)
            if res:
                return res
            res = self.dfs(node.right, target)
            if res:
                return res
        return None


    def isSameTree(self,p,q):
        if p is not None and q is not None:
            if p.val == q.val:
                if p.left is None and p.right is None and q.left is None and q.right is None:
                    return True
                else:
                    return (self.isSameTree(p.left, q.left)) and (self.isSameTree(p.right, q.right))
            else:
                return False
        elif p is None and q is None:
            return True
        return False
        


tree = TreeNode(7)
tree.left = TreeNode(4)
tree.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(19)

tree2 = TreeNode(7)
tree2.left = TreeNode(4)
tree2.right = TreeNode(3)
tree2.right.left = TreeNode(6)
tree2.right.right = TreeNode(19)

s = Solution()
res = s.getTargetCopy(tree, tree2, tree.right)   
print(res.val)     

tree = TreeNode(8)
tree.right = TreeNode(6)
tree.right.right = TreeNode(5)
tree.right.right.right = TreeNode(4)
tree.right.right.right.right = TreeNode(3)
tree.right.right.right.right.right = TreeNode(2)
tree.right.right.right.right.right.right = TreeNode(1)

tree2 = TreeNode(8)
tree2.right = TreeNode(6)
tree2.right.right = TreeNode(5)
tree2.right.right.right = TreeNode(4)
tree2.right.right.right.right = TreeNode(3)
tree2.right.right.right.right.right = TreeNode(2)
tree2.right.right.right.right.right.right = TreeNode(1)

s = Solution()
res = s.getTargetCopy(tree, tree2, tree2.right.right.right)   
print(res.val) 

tree = TreeNode(7)

tree2 = TreeNode(7)

s = Solution()
res = s.getTargetCopy(tree, tree2, tree2)   
print(res.val) 