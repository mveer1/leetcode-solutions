"""Given the head of a singly linked list, reverse the list, and return the reversed list.
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""
class ListNode:
    pass

# my sol: 
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        p = head
        while p is not None:
            nex = p.next
            p.next = prev

            prev = p
            p = nex
        
        return prev


# Approach #2 (Recursive) 
# public ListNode reverseList(ListNode head) {
#     if (head == null || head.next == null) return head;
#     ListNode p = reverseList(head.next);
#     head.next.next = head;
#     head.next = null;
#     return p;
# }