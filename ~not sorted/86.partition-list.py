#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # traverse the list with p 
        # if p is less than node, do nothing
        # if p is equal to the node or greater than that push
        # 1. push it forward
        # 2. append it directly to the end while marking the id of the first one to go the end, so we traverse the whole list only once.
        p = head
        while p is not None:
            p = p.next
        end = p

        prev = head
        p = head.next
        while id(p)==id(end):
            if prev.val < x:
                prev = prev.next
                p = p.next
            else:
                #store the val in temp
                #delete the node
                #insert a val at the end.
                temp = p.val
                

            

# @lc code=end

