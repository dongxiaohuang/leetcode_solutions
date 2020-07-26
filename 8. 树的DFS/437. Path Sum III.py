# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        return self.helper(root, sum, [sum])
    def helper(self, root, origin, targets):
        if not root:
            return 0
        
        hits = 0
        for target in targets:
            if target == root.val:
                hits += 1
        
        # update targets
        targets = [target-root.val for target in targets] +[origin]
        return hits + self.helper(root.left, origin, targets) + \
            self.helper(root.right, origin, targets)