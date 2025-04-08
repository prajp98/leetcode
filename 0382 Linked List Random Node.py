def __init__(self, head: Optional[ListNode]):
    self.head = head


def getRandom(self) -> int:
    scope = 1
    chosen = 0
    curr = self.head
    while curr:
        if random.random() < 1 / scope:
            chosen = curr.val
        curr = curr.next
        scope += 1
    return chosen