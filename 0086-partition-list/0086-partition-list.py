class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a = b = ListNode()
        c = d = ListNode()
        while head:
            if head.val < x:
                b.next = head
                b = b.next
            else:
                d.next = head
                d = d.next
            head = head.next
        d.next = None
        b.next = c.next
        return a.next