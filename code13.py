import collections


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def isPalindrome1(head) -> bool:
    q = collections.deque()
    if not head:
        return True
    node = head
    while node is not None:
        q.append(node.data)
        node = node.next
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    return True
def isPalindrome2(head) -> bool:
    slow = fast = head
    revers = None
    lead = head
    middle = None
    while fast and fast.next:
        fast = fast.next.next
        revers, revers.next, slow = slow, revers, slow.next
        trail = middle
        middle = lead
        lead = lead.next
        middle.next = trail
    if fast:
        slow = slow.next
    while revers and revers.data == slow.data:
        slow = slow.next
        revers = revers.next
    return not revers

node1 = Node(1)
print(isPalindrome1(node1))
node1.next = Node(2)
print(isPalindrome1(node1))
node1.next = Node(1)
print(isPalindrome2(node1))
