# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        else:
            return self.isSymHelper(root.left, root.right)
    
    def isSymHelper(self, root1: TreeNode, root2:TreeNode) -> bool:
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        elif root1.val != root2.val: return False
        else: return self.isSymHelper(root1.left, root2.right) and self.isSymHelper(root1.right, root2.left)