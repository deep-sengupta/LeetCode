class Solution:
    def reverseKGroup(self, head, k):
        d = ListNode(0, head)
        p = d
        while True:
            n = p
            for _ in range(k):
                n = n.next
                if not n:
                    return d.next
            a, b = p.next, n.next
            pre, cur = b, a
            while cur != b:
                cur.next, pre, cur = pre, cur, cur.next
            p.next, p = pre, a