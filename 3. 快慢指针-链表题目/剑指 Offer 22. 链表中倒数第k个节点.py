# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        slow = head
        fast = head
        if not head:
            return head
        for i in range(k):
            if fast:
                fast = fast.next
            else:
                return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
