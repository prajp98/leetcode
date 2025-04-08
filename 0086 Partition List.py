def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    left, right = ListNode(0), ListNode(0)
    lh, rh = left, right
    curr = head
    while curr:
        if curr.val < x:
            left.next = curr
            left = left.next
        else:
            right.next = curr
            right = right.next
        curr = curr.next
    right.next = None
    left.next = rh.next
    return lh.next
