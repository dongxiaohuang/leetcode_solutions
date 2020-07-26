# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        
        right_depth = self.get_depth(root.right)
        left_depth = self.get_depth(root.left)
        
        if abs(right_depth-left_depth) > 1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
            
    
    def get_depth(self, root):
        if not root: return 0
        return max(1+self.get_depth(root.right), 1+self.get_depth(root.left))