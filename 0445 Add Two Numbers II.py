def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def reverse(l):
        prev = None
        curr = l
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    l1 = reverse(l1)
    l2 = reverse(l2)
    carry = 0
    res = None
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        node = ListNode(total % 10)
        node.next = res
        res = node
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return res

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    s1,s2=[],[]
    while l1:
        s1.append(l1.val)
        l1=l1.next
    while l2:
        s2.append(l2.val)
        l2=l2.next
    carry=0
    res=None
    while s1 or s2 or carry:
        v1=s1.pop() if s1 else 0
        v2=s2.pop() if s2 else 0
        total=v1+v2+carry
        carry=total//10
        node=ListNode(total%10)
        node.next=res
        res=node
    return res