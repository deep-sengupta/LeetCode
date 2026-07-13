class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        n, tail = 1, head
        while tail.next:
            tail, n = tail.next, n + 1
        k %= n
        if not k:
            return head
        tail.next = head
        cur = head
        for _ in range(n - k - 1):
            cur = cur.next
        head = cur.next
        cur.next = None
        return head