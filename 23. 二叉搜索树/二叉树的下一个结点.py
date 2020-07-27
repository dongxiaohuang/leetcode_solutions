# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, root):
        # write code here
        if not root:
            return None
        if root.right:
            res = root.right
            while res and res.left:
                res = res.left
            return res
        if root.next:
            parent = root
            while parent.next and parent.next.left != parent:
                parent = parent.next
            #if parent.next and parent.next.left == parent:
            return parent.next
        
        return None