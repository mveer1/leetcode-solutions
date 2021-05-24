""""Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
array form example, for num = 1321, the array form is [1,3,2,1].

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
"""
# mysol:
class Solution:
    def addToArrayForm(self, A: list[int], K: int) -> list[int]:
        return list(str(int("".join([str(c) for c in A]))+K))

# better: H
class Solution(object):
    def addToArrayForm(self, A, K):
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i: A[i-1] += carry
        if carry:
            A = map(int, str(carry)) + A
        return A