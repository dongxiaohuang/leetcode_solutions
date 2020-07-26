# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, root1, root2):
        # write code here
        if not root1 or not root2:
            return False
        res = False
        if root1.val == root2.val:
            if self.helper(root1, root2) :
                return True
        if self.HasSubtree(root1.left, root2):
            return True
        if self.HasSubtree(root1.right, root2):
            return True
        return False
    
    def helper(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 and root2:
            return False
        if root1 and not root2:
            return True
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.left) and self.helper(root1.right, root2.right)