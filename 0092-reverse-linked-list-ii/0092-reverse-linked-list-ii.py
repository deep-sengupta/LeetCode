class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        p = d
        for _ in range(left - 1):
            p = p.next
        c = p.next
        for _ in range(right - left):
            t = c.next
            c.next = t.next
            t.next = p.next
            p.next = t
        return d.next