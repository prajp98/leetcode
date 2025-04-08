def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    curr = head
    n = 0
    while curr:
        n += 1
        curr = curr.next
    div, rem = divmod(n, k)
    res = []
    curr = head
    for i in range(k):
        h = curr
        size = div + (1 if i < rem else 0)
        for j in range(size - 1):
            if curr:
                curr = curr.next
        if curr:
            t = curr.next
            curr.next = None
            curr = t
        res.append(h)
    return res