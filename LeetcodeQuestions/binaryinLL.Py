"""binaryinLL.Py

1290. Convert Binary Number in a Linked list to Integer
Return the decimal value of the number in the linked list.
"""

# mysol:
# Definition for singly-linked list.
class listNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: listNode) -> int:
        p = head
        l = []
        binary = 0
        while p is not None:
            l.append(p.val)
            p = p.next
        leng = len(l)
        for i in l:
            binary += (2**(leng-1))*i
            leng -= 1
        return binary


# official sol:
# better:
# Approach 1: Binary Representation
class Solution:
    def getDecimalValue(self, head: listNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val
            head = head.next
        return num


# better:
# Approach 2: Bit Manipulation
class Solution:
    def getDecimalValue(self, head: listNode) -> int:
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val
            head = head.next
        return num

# both time O(N) and const space
