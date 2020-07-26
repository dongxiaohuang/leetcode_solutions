class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        fast = slow = head
        rev_head = ListNode(-1)
        while fast and fast.next:
            fast = fast.next.next
            rev_next = rev_head.next
            rev_head.next = slow
            print(slow.val)
            slow = slow.next
            rev_head.next.next = rev_next
        if fast:
            slow = slow.next
        
        rev_head = rev_head.next
        while slow and rev_head:
            if slow.val != rev_head.val:
                return False
            slow = slow.next
            rev_head = rev_head.next
        return True