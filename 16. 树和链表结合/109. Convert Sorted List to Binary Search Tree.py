# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        prev_slow = ListNode(-1)
        prev_slow.next = head
        slow = fast = head
        while fast and fast.next:
            prev_slow = prev_slow.next
            slow = slow.next
            fast = fast.next.next
        root = ListNode(slow.val)
        root.right = self.sortedListToBST(slow.next)
        prev_slow.next = None
        root.left = self.sortedListToBST(head)
        return root