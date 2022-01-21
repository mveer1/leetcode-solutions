
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.


class ListNode:
    pass

def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    temp=101
    a=ListNode()
    if head:
        a=head
        a=head.next
        b=ListNode()
        b=head
        while a:
            if a.val==b.val:
                b.next=a.next
                a=a.next
            else:
                b=b.next
                a=a.next
        return head
    else:
        return head

# mysol: 
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