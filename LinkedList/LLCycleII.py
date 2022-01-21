"""Linked List Cycle II
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
"""

class ListNode:
    pass
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:          
        slow = fast = head
        if slow == None or slow.next == None:
            return None
        
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                len_rem = 0
                p = head
                while p!=slow:
                    len_rem+=1
                    p = p.next
                    slow = slow.next
            
                #pass slow to a funciton which uses it to find start of the list.
                p=head
                for _ in range(len_rem):
                    p = p.next
                return p
        return None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = node = head
        
        # Figure out if there's a cycle and first-intersection
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast: break
        else:
            return None
        
        # Find cycle entrance
        while node is not slow:
            node, slow = node.next, slow.next
        return node
