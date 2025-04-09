def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return

    def merge(l1, l2):
        dummy = curr = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

    while len(lists) > 1:
        newList = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            newList.append(merge(l1, l2))
        lists = newList
    return lists[0]

def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i,node in enumerate(lists):
        if node:
            heapq.heappush(heap,(node.val,i,node))
    dummy = curr = ListNode()
    while heap:
        val,i,node=heapq.heappop(heap)
        curr.next=node
        curr=curr.next
        if node.next:
            heapq.heappush(heap,(node.next.val,i,node.next))
    return dummy.next
