class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
def mergeTwoLists(l1: Node, l2: Node) -> Node:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1

a = Node(1)
a.next = Node(3)
a.next.next = Node(5)
b = Node(2)
b.next = Node(4)
b.next.next = Node(6)
c = mergeTwoLists(a, b)
while c:
    print(c.val)
    c = c.next