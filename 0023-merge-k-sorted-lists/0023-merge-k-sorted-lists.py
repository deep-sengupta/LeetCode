from heapq import *

class Solution:
    def mergeKLists(self, lists):
        h=[]
        for i,n in enumerate(lists):
            if n: heappush(h,(n.val,i,n))
        d=t=ListNode()
        while h:
            _,i,n=heappop(h)
            t.next=t=n
            if n.next: heappush(h,(n.next.val,i,n.next))
        return d.next