# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        end = dummy
        for i in range(m-1):
            prev = prev.next
        for j in range(n+1):
            end = end.next
        tail = prev.next

        cur = tail.next
        while tail.next != end:
            next_cur = cur.next
            cur.next = prev.next
            prev.next = cur
            tail.next = next_cur
            cur = next_cur

        return dummy.next
