class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth and right_depth:
            return min(left_depth, right_depth)+1
        elif not left_depth:
            return right_depth+1
        else:
            return left_depth+1
