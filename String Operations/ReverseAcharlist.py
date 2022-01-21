"""Write a function that reverses a string. The input string is given as an array of characters s.
Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
# mysol:
# s.reverse()

"""Approach 1: Recursion, In-Place, O(N) Space

Does in-place mean constant space complexity?
No. By definition, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure.
The tricky part is that space is used by many actors, not only by data structures. The classical example is to use recursive function without any auxiliary data structures.
Is it in-place? Yes.
Is it constant space? No, because of recursion stack.
"""
class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)



# Approach 2: Two Pointers, Iteration, O(1) Space
class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1
