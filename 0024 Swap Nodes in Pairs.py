def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = prev = ListNode()
    dummy.next = curr = head
    while curr and curr.next:
        one = curr
        two = curr.next
        prev.next = two
        one.next = two.next
        two.next = one
        prev = curr
        curr = curr.next
    return dummy.next