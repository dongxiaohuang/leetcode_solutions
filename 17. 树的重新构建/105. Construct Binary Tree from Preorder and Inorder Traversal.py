# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        rootValue = preorder[0]
        root = TreeNode(rootValue)
        inorderIndex = inorder.index(rootValue)

        root.left = self.buildTree(
            preorder[1:inorderIndex+1], inorder[:inorderIndex])
        root.right = self.buildTree(
            preorder[inorderIndex+1:], inorder[inorderIndex+1:])

        return root
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# buildTree( preorder, inorder)
