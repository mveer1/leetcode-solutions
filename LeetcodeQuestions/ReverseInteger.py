# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        sx=str(x)
        if sx[0]=="-":
            sx="-"+ sx[::-1]
            if int(sx[0:-1]) > 2147483647 or int(sx[0:-1]) < -2147483648:
                return 0
            else: 
                return int(sx[0:-1])
        if int(sx[::-1]) > 2147483647 or int(sx[::-1]) < -2147483648:
            return 0
        else:
            return int(sx[::-1])

