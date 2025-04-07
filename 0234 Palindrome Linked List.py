def isPalindrome(self, head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    l, r = head, prev
    while r:
        if l.val != r.val:
            return False
        l = l.next
        r = r.next
    return True