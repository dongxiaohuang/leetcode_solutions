# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res = []
        self.in_order(pRoot, res, k)
        if k <= 0 or k > len(res):
            return None
        return res[k-1]

    def in_order(self, root, res, k):
        if not root:
            return
        self.in_order(root.left, res, k)
        res.append(root)
        if len(res) == k:
            return
        self.in_order(root.right, res, k)
