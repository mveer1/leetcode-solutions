"""Kth Missing Positive Number
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.

Input: arr = [2,3,4,7,11], k = 5
Output: 9

Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9
"""
# Mysol
# 48ms
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        s = set()
        for i in range(k+len(arr)+5):
            s.add(i)
        rem = s-set(arr)
        rem = sorted(list(rem))
        return rem[k]


# 48ms
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        Val,i,count,Set = 0,1,0,set(arr)
        while True:
            if count == k:
                return Val
            if i not in Set:
                Val = i
                count += 1
            i += 1  



# 32ms
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if k <= arr[m] - (m + 1):
                r = m - 1
            else:
                l = m + 1
        # return k - (arr[r] - (r + 1)) + arr[r]
        return k + l
