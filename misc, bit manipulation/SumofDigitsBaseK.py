"""1837. Sum of Digits in Base K
Given an integer n (in base 10) and a base k, return the sum of the digits of n after converting n from base 10 to base k.

After converting, each digit should be interpreted as a base 10 number, and the sum should be returned in base 10.
"""
# mysol
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = [0]*7        #cos constraints tell us max is 100 in base 2, which is 7 digits
        i = 0
        while n > 0:
            ans[i] = n % k
            n //= k
            i +=1         
            
        print(ans)
        res = 0
        for a in ans:
            res+=int(a)
        return res
        

# mysol (better) 99.47, 80%:
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        sum = 0
        while n > 0:
            sum += n % k
            n //= k
        return sum
