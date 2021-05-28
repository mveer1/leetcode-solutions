"""172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.
Follow up: Could you write a solution that works in logarithmic time complexity?
"""
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Trailing 0s in n! = Count of 5s in prime factors of n!
        #                   = floor(n/5) + floor(n/25) + floor(n/125) + ....
        i=5
        count = 0
        while (n / i>= 1):
            count += n // i
            i *= 5
        return count

# similar:
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
 
    # Keep dividing n by
    # 5 & update Count
        while(n >= 5):
            n //= 5
            count += n

        return count
