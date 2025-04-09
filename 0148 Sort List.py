def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def getMid(head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(l1, l2):
        dummy = tail = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next

    def mergeSort(head):
        if not head or not head.next:
            return head
        mid = getMid(head)
        left = head
        right = mid.next
        mid.next = None
        ls = mergeSort(left)
        rs = mergeSort(right)
        return merge(ls, rs)

    return mergeSort(head)
