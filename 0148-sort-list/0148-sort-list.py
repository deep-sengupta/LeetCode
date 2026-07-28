class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        s = f = head
        while f.next and f.next.next:
            s, f = s.next, f.next.next
        m = s.next
        s.next = None
        l, r = self.sortList(head), self.sortList(m)
        d = t = ListNode()
        while l and r:
            if l.val < r.val:
                t.next, l = l, l.next
            else:
                t.next, r = r, r.next
            t = t.next
        t.next = l or r
        return d.next