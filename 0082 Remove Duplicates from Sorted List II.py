def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = prev = ListNode()
    dummy.next = curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next
            curr = curr.next
        else:
            prev = prev.next
            curr = curr.next
    return dummy.next