"""234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome."""

# mysol  45%
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next == None:
            return True
        mid = fast = head
        store = [head.val]
        
        while True:
            if fast == None:
                store.pop()
                break
            if fast.next == None:
                break
            mid = mid.next
            fast = fast.next.next
            store.append(mid.val)


            
        c = len(store)-1
        while mid:
            if mid.val != store[c]:
                return False
            mid = mid.next
            c -=1
        return True




class Solution: #90%
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast, rev = head, head, None

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        while slow:
            if slow.val != rev.val:
                return False
            slow = slow.next
            rev = rev.next
        return True


    


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        prev = None
        
        while fast and fast.next:
            fast= fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow 
            slow = temp 
            
        if fast:
            slow = slow.next
        
        while prev:
            if prev.val != slow.val:
                return False
            
            prev = prev.next
            slow = slow.next
        
        return True








        