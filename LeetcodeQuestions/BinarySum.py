"""
Given two binary strings a and b, return their sum as a binary string.
Example 1:

Input: a = "11", b = "1"
Output: "100"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry=0
        result=""
        if len(a)<=len(b):
            a="0"*(len(b)-len(a))+a
        else:
            b="0"*(len(a)-len(b))+b
        
        for i,j in zip(a[::-1], b[::-1]):
            if int(i)+int(j)+carry==0:
                result+=str(0)
                carry=0
            elif int(i)+int(j)+carry==1:
                result+=str(1)
                carry=0
            elif int(i)+int(j)+carry==2:
                result+=str(0)
                carry=1
            else:
                result+=str(1)
                carry=1
        result+=str(carry)
        return str(int(result[::-1]))
