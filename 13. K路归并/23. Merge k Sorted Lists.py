# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        minq = []
        i = 0
        for _list in lists:
            if _list:
                heapq.heappush(minq, (_list.val, i, _list))
                i += 1
        dummy = ListNode(-1)
        cur = dummy
        while minq:
            val, _, node = heapq.heappop(minq)
            if node.next:
                heapq.heappush(minq, (node.next.val, i, node.next))
                i += 1
            cur.next = node
            cur = cur.next
        return dummy.next
