class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        node_dict = {}
        while pHead1:
            node_dict[pHead1] = 1
            pHead1 = pHead1.next
        while pHead2:
            if pHead2 in node_dict:
                return pHead2
            pHead2 = pHead2.next
        return None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1