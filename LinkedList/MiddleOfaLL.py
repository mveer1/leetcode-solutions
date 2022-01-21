"""876. Middle of the Linked list
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""
# mysol:
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next != None:
            if fast.next.next == None:
                return slow.next
            slow = slow.next
            fast = fast.next.next
        return slow



# official sol
# Time Complexity: O(N)O(N), where NN is the number of nodes in the given list.
# Space Complexity: O(N)O(N), the space used by A.
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        arr = [head]
        while arr[-1].next:
            arr.append(arr[-1].next)
        return arr[len(arr) // 2]




# Approach 2: Fast and Slow Pointer
# O(N) time and O(1) space
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow