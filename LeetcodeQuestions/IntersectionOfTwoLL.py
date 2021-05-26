"""160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

It is guaranteed that there are no cycles anywhere in the entire linked structure.
"""


# mysol

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1 = headA
        
        while p1!=None:
            p2 = headB
            while p2!=None:
                if id(p1)==id(p2):
                    return p1
                p2 = p2.next
            p1 = p1.next
        return None




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hashset = set()
        p1 = headA
        while p1 != None:
            hashset.add(id(p1))
            p1 = p1.next
            
        p2 = headB
        while p2 != None:
            if id(p2) in hashset:
                return p2
            p2 = p2.next
        return None


        

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Method 1(Simply use two loops) (what I did) Time O(M*N)

Method 2 (Mark Visited Nodes) Time O(M+N)

    This solution requires modifications to basic linked list data structure. 
    Have a visited flag with each node. 
    Traverse the first linked list and keep marking visited nodes.
    Now traverse the second linked list, If you see a visited node again then there is an intersection point,return the intersecting node. 
    This solution works in O(m+n) but requires additional information with each node.

    A variation of this solution that doesn’t require modification to the basic data structure can be implemented using a hash. 
    Traverse the first linked list and store the addresses of visited nodes in a hash.
    Now traverse the second linked list and if you see an address that already exists in the hash then return the intersecting node.


Method 3(Using difference of node counts (size of LL))         Time Complexity: O(m+n)  Auxiliary Space: O(1)

    Get the difference of counts d = abs(c1 – c2)
    Now traverse the bigger list from the first node till d nodes 
        so that from here onwards both the lists have equal no of nodes 
    Then we can traverse both the lists in parallel till we come across a common node. 


Method 4 (Make circle in first list)                            Time Complexity: O(m+n) Auxiliary Space: O(1)

    1. Traverse the first linked list(count the elements) and make a circular linked list. 
        (Remember the last node so that we can break the circle later on). 
    2. Now view the problem as finding the loop in the second linked list. So the problem is solved.

    3. Since we already know the length of the loop(size of the first linked list) 
        we can traverse those many numbers of nodes in the second list, 
        and then start another pointer from the beginning of the second list. 
        we have to traverse until they are equal, and that is the required intersection point. 
    4. remove the circle from the linked list. 


Method 5 (Reverse the first list and make equations)            Time complexity: O(m+n) Auxiliary Space: O(1)

    1) Let X be the length of the first linked list until intersection point.
    Let Y be the length of the second linked list until the intersection point.
    Let Z be the length of the linked list from the intersection point to End of the linked list including the intersection node.
    We Have
            X + Z = C1;
            Y + Z = C2;

    2) Reverse first linked list.
    3) Traverse Second linked list. Let C3 be the length of second list - 1. 
        Now we have
            X + Y = C3
        We have 3 linear equations. By solving them, we get
        X = (C1 + C3 – C2)/2;
        Y = (C2 + C3 – C1)/2;
        Z = (C1 + C2 – C3)/2;
        WE GOT THE INTERSECTION POINT.
    4)  Reverse first linked list again.

    Advantage: No Comparison of pointers. 
    Disadvantage : Modifying linked list(Reversing list). 

Method 7 (Use Hashing)         This method required O(n) additional space and not very efficient if one list is large.
    Basically, we need to find a common node of two linked lists. 
    So we hash all nodes of the first list and then check the second list. 

    1) Create an empty hash set. 
    2) Traverse the first linked list and insert all nodes’ addresses in the hash set. 
    3) Traverse the second list. For every node check if it is present in the hash set. 
       If we find a node in the hash set, return the node.


Method 8 (2-pointer technique):      Time complexity : O( m + n )   Auxiliary Space:  O(1)
    1. Initialize two pointers ptr1 and ptr2  at the head1 and  head2.
    2. Traverse through the lists,one node at a time.
    3. When ptr1 reaches the end of a list, then redirect it to the head2.
    4. similarly when ptr2 reaches the end of a list, redirect it the head1.
    5. Once both of them go through reassigning,hey will be equidistant from the collision point
    6. If at any node ptr1 meets ptr2, then it is the intersection node.
        After second iteration if there is no intersection node it returns NULL.
"""

