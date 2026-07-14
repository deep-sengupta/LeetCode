class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode(0, head)
        p = d
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                p.next = head.next
            else:
                p = p.next
            head = head.next
        return d.next