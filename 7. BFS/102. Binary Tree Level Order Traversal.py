# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        while q:
            tmp_res = []
            tmp_len = len(q)
            while tmp_len:
                node = q.pop(0)
                tmp_res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp_len -= 1
            res.append(tmp_res)
        return res