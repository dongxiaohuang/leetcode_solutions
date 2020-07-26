class Solution(object):
    def partition(self, head, x):
        before = before_head = ListNode(-1)
        after = after_head = ListNode(-1)

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        before.next = after_head.next
        after.next = None
        return before_head.next
