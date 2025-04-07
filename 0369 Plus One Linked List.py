def plusOne(self, head: ListNode) -> ListNode:
    dummy = ListNode()
    dummy.next = curr = head
    notNine = dummy
    while curr:
        if curr.val != 9:
            notNine = curr
        curr = curr.next
    notNine.val += 1
    notNine = notNine.next
    while notNine:
        notNine.val = 0
        notNine = notNine.next
    return dummy.next