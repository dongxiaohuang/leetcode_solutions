class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        if t.left is None and t.right is None:
            return "{}".format(t.val)
        elif t.right is None:
            return "{}({})".format(t.val, self.tree2str(t.left))
        elif t.left is None:
            return "{}()({})".format(t.val, self.tree2str(t.right))
        else:
            return "{}({})({})".format(t.val, self.tree2str(t.left), self.tree2str(t.right))