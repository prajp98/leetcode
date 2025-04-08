def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    dummy = ListNode()
    while curr:
        nxt = curr.next
        prev = dummy
        while prev.next and prev.next.val < curr.val:
            prev = prev.next
        curr.next = prev.next
        prev.next = curr
        curr = nxt
    return dummy.next