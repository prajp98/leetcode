def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    oldToCopy = {}
    curr = head
    if not head:
        return
    while curr:
        oldToCopy[curr] = Node(curr.val)
        curr = curr.next
    curr = head
    while curr:
        copy = oldToCopy[curr]
        copy.next = oldToCopy.get(curr.next, None)
        copy.random = oldToCopy.get(curr.random, None)
        curr = curr.next
    return oldToCopy[head]