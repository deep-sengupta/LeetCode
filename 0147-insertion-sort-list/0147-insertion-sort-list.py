class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0)
        while head:
            p = d
            while p.next and p.next.val < head.val:
                p = p.next
            head.next, p.next, head = p.next, head, head.next
        return d.next