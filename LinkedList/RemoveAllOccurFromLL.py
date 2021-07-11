"""203. Remove Linked List Elements

Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = head
        prev = None
        # If head node itself holds the key or multiple occurrences of key
        while (temp != None and temp.val == val):
            head = temp.next   # Changed head
            temp = head        # Change Temp
            
        # Delete ocurrences other than head
        while (temp != None):
            # Search for the val to be deleted,
            # keep track of the previous node
            # as we need to change 'prev.next'
            while (temp != None and temp.val != val):
                prev = temp
                temp = temp.next
                
            # If val was not present in linked list
            if (temp == None):
                return head

            # Unlink the node from linked list
            prev.next = temp.next

            # Update Temp for next iteration of outer loop
            temp = prev.next
        return head





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        dummy=ListNode(-1,head)
        prev=dummy
        curr=head
        while curr:
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
           
        return dummy.next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = ListNode()
        curr.next = head
        dummy = curr
        
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next