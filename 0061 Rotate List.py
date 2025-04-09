def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    n = 1
    tail = head
    while tail.next:
        n += 1
        tail = tail.next
    curr = head
    k = k % n
    if k == 0:
        return head
    for i in range(n - k - 1):
        curr = curr.next
    nxt = curr.next
    curr.next = None
    tail.next = head
    return nxt