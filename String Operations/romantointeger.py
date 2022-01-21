
"""Given a roman numeral, convert it to an integer.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        prev = 0
        curr = 0
        total = 0
        for i in range(len(s)):
            curr = dic[s[i]]
            if curr > prev:
                total = total + curr - 2* prev
            else:
                total = total + curr
            prev=curr
        return total


class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        val=0
        for i in range(len(s)-1):
            if roman[s[i]]>=roman[s[i+1]]:
                val+=roman[s[i]]
            else:
                val-=roman[s[i]]
        return val+roman[s[-1]]
 