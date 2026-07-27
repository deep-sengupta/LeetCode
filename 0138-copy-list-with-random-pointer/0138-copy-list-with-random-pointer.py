class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        dummy = Node(0)
        copy_curr = dummy
        curr = head

        while curr:
            copy_curr.next = curr.next
            copy_curr = copy_curr.next
            curr.next = curr.next.next
            curr = curr.next

        return dummy.next