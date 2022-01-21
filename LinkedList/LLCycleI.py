"""Linked List Cycle I
Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true

Input: head = [1,2], pos = 0
Output: true"""


class ListNode:
    pass

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        if slow == None:
            return False    
        if slow.next == None:   #only one node or no node at all
            return False
        
        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False