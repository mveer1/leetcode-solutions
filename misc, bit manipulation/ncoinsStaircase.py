"""You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""

# mysol: not good, 900ms
class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        i = 1
        while res<=n:
            res += i
            i+=1
        return i-2


# Approach 1: Binary Search logn  40ms
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right


# Approach 2: Math   O(1)   24ms
"""k(k+1)≤2N
find k by squaring both sides and:
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
