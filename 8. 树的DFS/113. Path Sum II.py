# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def pathSum(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        self.helper(root, res, expectNumber, [])
        return res
    
    def helper(self, root, res, target, tmp):
        if not root:
            return 
        tmp.append(root.val)
        if not root.left and not root.right and root.val == target:
            res.append(list(tmp))
        else:
            target = target- root.val
            self.helper(root.left, res, target, tmp)
            self.helper(root.right, res, target, tmp)
        tmp.pop()