# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = []
        reverse = False
        q.append(root)
        while q:
            tmp = []
            count = len(q)
            print([_q.val for _q in q])
            while count:
                count -= 1
                node = q.pop(0)
                tmp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                tmp = tmp[::-1]
            reverse = not reverse
            res.append(tmp)
        return res
                