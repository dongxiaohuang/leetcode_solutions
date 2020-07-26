class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy_rev = ListNode(-1)
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev_next = dummy_rev.next
            dummy_rev.next = slow
            slow = slow.next
            dummy_rev.next.next = rev_next
        if fast:
            slow = slow.next

        rev = dummy_rev.next
        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
        return True
