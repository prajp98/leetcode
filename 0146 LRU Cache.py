class Node:
    def __init__(self, key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dict={}
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node=self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            oldNode=self.dict[key]
            self.remove(oldNode)
        node=Node(key,value)
        self.dict[key]=node
        self.add(node)
        if len(self.dict)>self.capacity:
            lru=self.tail.prev
            self.remove(lru)
            del self.dict[lru.key]
    def remove(self,node):
        p=node.prev
        n=node.next
        p.next=n
        n.prev=p
    def add(self,node):
        n=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=n
        n.prev=node
