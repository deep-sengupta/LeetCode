class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = f = head
        while f and f.next:
            s, f = s.next, f.next.next
            if s == f:
                while head != s:
                    head, s = head.next, s.next
                return head
        return None