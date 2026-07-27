class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = head
        while f and f.next:
            s, f = s.next, f.next.next
        p, c = None, s.next
        s.next = None
        while c:
            c.next, p, c = p, c, c.next
        while p:
            head.next, p.next, head, p = p, head.next, head.next, p.next