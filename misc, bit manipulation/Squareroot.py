
# Given a non-negative integer x, compute and return the square root of x
class Solution:
    def mySqrt(self, x: int) -> int:
        if x<1:
            return x
        g=x/6
        for i in range(18):
            r=((x/g) + g)/2
            g=r
        return int(r)
