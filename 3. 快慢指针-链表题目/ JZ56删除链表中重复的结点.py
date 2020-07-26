class Solution:
    def deleteDuplication(self, head):

        # write code here
        if not head or not head.next:
            return head
        dummy = ListNode(head.val-1)
        prev = dummy
        dummy.next = head
        cur = head
        while cur:
            if cur and cur.next and cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next
