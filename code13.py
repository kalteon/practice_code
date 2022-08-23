class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def isPalindrome(head) -> bool:
    q = []
    if not head:
        return True
    node = head
    while node is not None:
        q.append(node.data)
        node = node.next
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    return True
node1 = Node(1)
print(isPalindrome(node1))
node1.next = Node(2)
print(isPalindrome(node1))
node1.next = Node(1)
print(isPalindrome(node1))
