def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = prevLeft = ListNode()
    dummy.next = curr = head
    for i in range(left - 1):
        prevLeft = curr
        curr = curr.next
    prev = None
    for i in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    prevLeft.next.next = curr
    prevLeft.next = prev
    return dummy.next