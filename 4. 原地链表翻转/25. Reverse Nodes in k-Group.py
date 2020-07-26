# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while(prev):
            prev = self.reverse(prev, k)

        return dummy.next

    def reverse(self, prev, k):
        last = prev
        for i in range(k+1):
            last = last.next
            if not last and i != k:
                return None

        tail = prev.next
        cur = tail.next
        while tail.next != last:
            _next = cur.next
            cur.next = prev.next
            prev.next = cur
            tail.next = _next
            cur = _next
            # print(prev.next)
        return tail
