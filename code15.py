class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
def reverseList(head: Node) -> Node:
    trail = middle = None
    lead = head
    while lead:
        trail = middle
        middle = lead
        lead = lead.next
        middle.next = trail
    return middle

a = Node(0)
b = a
for i in range(1, 6):
    b.next = Node(i)
    b = b.next
c = reverseList(a)
while c:
    print(c.val)
    c = c.next