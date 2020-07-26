class Solution:
    # 返回 RandomListNode
    def Clone(self, head):
        # write code here
        if not head:
            return head
        dummy = RandomListNode(-1)
        old2new = {}
        cur = head
        new_cur = dummy
        while cur:
            new_node = RandomListNode(cur.label)
            old2new[cur] = new_node
            new_node.random = cur.random
            new_cur.next = new_node
            new_cur = new_cur.next
            cur = cur.next
        cur = dummy.next
        while cur:
            if cur.random:
                cur.random = old2new[cur.random]
            cur = cur.next
        return dummy.next

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return head
        cur = head
        while cur:
            new_node = Node(cur.val,None,None)   # 克隆新结点
            new_node.next = cur.next
            cur.next = new_node   # 克隆新结点在cur 后面
            cur = new_node.next   # 移动到下一个要克隆的点
        cur = head

        while cur:  # 链接random
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur_old_list = head # 将两个链表分开
        cur_new_list = head.next
        new_head = head.next
        while cur_old_list:
            cur_old_list.next = cur_old_list.next.next
            cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
            cur_old_list = cur_old_list.next
            cur_new_list = cur_new_list.next
        return new_head

作者：z1m
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。