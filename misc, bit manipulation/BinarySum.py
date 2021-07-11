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




class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = -1
        carry = 0
        l = [None]*(max(len(a), len(b))+1)
        while True:
            try:
                if int(a[i])+int(b[i])+carry==0:
                    l[i] = "0"
                    carry = 0
                elif int(a[i])+int(b[i])+carry==1:
                    l[i] = "1"
                    carry = 0
                elif int(a[i])+int(b[i])+carry==2:
                    l[i] = "0"
                    carry = 1
                else:
                    l[i] = "1"
                    carry = 1
            except IndexError:
                if len(a)-len(b)<0:
                    for _ in range(len(b)-len(a)):
                        if int(b[i])+carry==0:
                            l[i] = "0"
                            carry= 0
                        elif int(b[i])+carry==1:
                            l[i] = "1"
                            carry= 0
                        else:
                            l[i] = "0"
                            carry= 1
                        i -= 1
                    if carry == 1 and l[0] is None:
                        l[0]="1"
                        return str(int("".join(l)))
                    elif carry == 0 and l[0] is None:
                        l[0]="0"
                        return str(int("".join(l)))
                    else:
                        return str(int("".join(l)))
                else:
                    for _ in range(len(a)-len(b)):
                        if int(a[i])+carry==0:
                            l[i] = "0"
                            carry= 0
                        elif int(a[i])+carry==1:
                            l[i] = "1"
                            carry= 0
                        else:
                            l[i] = "0"
                            carry= 1
                        i -= 1
                    if carry == 1 and l[0] is None:
                        l[0]="1"
                        return str(int("".join(l)))
                    elif carry == 0 and l[0] is None:
                        l[0]="0"
                        return str(int("".join(l)))
                    else:
                        return str(int("".join(l)))
            i -= 1






class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        max_len = max(len(a), len(b))
        
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        ans = []
        
        carry = '0'
        for i in range(max_len-1,-1,-1):
            if a[i] == '1' and b[i] == '1':
                ans.append(carry)
                carry = '1'
            elif a[i] == '1' or b[i] == '1':
                if carry == '1':
                    ans.append('0')
                else:
                    ans.append('1')
            else:
                ans.append(carry)
                carry = '0'
                
        if carry == '1':
            ans.append(carry)

        return ''.join(ans[::-1])