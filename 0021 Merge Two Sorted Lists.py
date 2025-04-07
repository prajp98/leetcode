def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    p1, p2 = list1, list2
    dummy = curr = ListNode()
    while p1 and p2:
        if p1.val <= p2.val:
            curr.next = ListNode(p1.val)
            p1 = p1.next
        else:
            curr.next = ListNode(p2.val)
            p2 = p2.next
        curr = curr.next
    if p1:
        curr.next = p1
    if p2:
        curr.next = p2
    return dummy.next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    p1,p2=list1,list2
    dummy=curr=ListNode()
    while p1 and p2:
        if p1.val<=p2.val:
            curr.next=p1
            p1=p1.next
        else:
            curr.next=p2
            p2=p2.next
        curr=curr.next
    if p1:
        curr.next=p1
    if p2:
        curr.next=p2
    return dummy.next