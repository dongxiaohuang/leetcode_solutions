# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, root):
        # write code here
        if not root:
            return None
        if not root.left and not root.right:
            return root
        left = root.left
        self.Convert(root.left)
        
        if left:
            while left.right:
                left = left.right
            root.left, left.right = left, root
        self.Convert(root.right)
        right = root.right
        if right:
            while right.left:
                right = right.left
            right.left, root.right = root, right
        while root.left:
            root = root.left
        return root