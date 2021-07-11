"""83. Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def delete(self,n):
        if n.next is None:
            return
        n.next = n.next.next
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return
        prev = head
        p = head.next
        
        while(p is not None):
            if p.val == prev.val:
                self.delete(prev)     #deletes p only, but we pass a element of left
                p = p.next
            else:
                prev = p
                p = p.next
            
        return head





"""
public ListNode deleteDuplicates(ListNode head) {
    ListNode current = head;
    while (current != null && current.next != null) {
        if (current.next.val == current.val) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }
    return head;
}



Time complexity : O(n)O(n). Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is O(n)O(n), where nn is the number of nodes in the list.

Space complexity : O(1)O(1). No additional space is used."""










# https://www.geeksforgeeks.org/remove-duplicates-from-a-sorted-linked-list/