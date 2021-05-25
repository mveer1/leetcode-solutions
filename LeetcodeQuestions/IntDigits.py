"""Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

num = 38
Output: 2
"""

# mysol:
class Solution:
    def addDigits(self, num: int) -> int:
        string = str(num)
        res = int(string)
        while(res>9):
            res = 0
            for s in string:
                res+=int(s)
            string = str(res)
        return res

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num%9 == 0:
            return 9
        return num%9
"""
which is same as
return 1 + (num - 1) % 9 if num else 0
"""