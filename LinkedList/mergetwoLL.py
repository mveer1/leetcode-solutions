"""Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists
Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

my solution: 32ms
"""
class listNode:
    pass

class Solution:
    def mergeTwolists(self, l1: listNode, l2: listNode) -> listNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        p = l1
        q = l2
        
        if p.val <= q.val:
            ll1 = l1
            p = p.next
        else: 
            ll1 = l2
            q = q.next
        
        prev = ll1
        
        while(True):
            
            if p is None:
                prev.next = q
                break
            elif q is None:
                prev.next = p
                break
            
            if p.val <= q.val:
                prev.next = p
                prev = p
                p = p.next
            else: 
                prev.next = q
                prev = q
                q = q.next

        return ll1


def mergeTwolists(self, l1: listNode, l2: listNode) -> listNode:
	if not l1:
		return l2
	if not l2:
		return l1
	l1listNode = l1
	l2listNode = l2
	resultNode = listNode(0)
	returnHead = resultNode
	while l1listNode and l2listNode:
		if l1listNode.val <= l2listNode.val:
			resultNode.next = l1listNode
			l1listNode = l1listNode.next
		else:
			resultNode.next = l2listNode
			l2listNode = l2listNode.next
		resultNode = resultNode.next


	if not l1listNode and l2listNode:
		resultNode.next = l2listNode
	elif not l2listNode and l1listNode:
		resultNode.next = l1listNode
	return returnHead.next
