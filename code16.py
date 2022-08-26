class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def addTwoBynbers(l1, l2) -> Node:
    carry = 0
    l3 = tempNode = Node()
    while l1 or l2 or carry:
        if l1:
            digit1 = l1.val
            l1 = l1.next
        else:
            digit1 = 0
        if l2:
            digit2 = l2.val
            l2 = l2.next
        else:
            digit2 = 0
        temp = digit1 + digit2 + carry
        carry = temp // 10
        temp %= 10
        tempNode.next = Node(temp)
        tempNode = tempNode.next
    return l3.next
a = Node(9)
a.next = Node(9)
a.next.next = Node(9)
b = Node(9)
c = addTwoBynbers(a, b)
while c:
    print(c.val)
    c = c.next