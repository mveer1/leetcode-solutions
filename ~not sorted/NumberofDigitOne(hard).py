"""233. Number of Digit One
Hard
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

mysol: 
"""
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while(i <= n):
            j = i * 10
            count += ((n // j) * i + min(max(n % j -i + 1, 0), i))
            i *= 10

        return count

"""Approach #2 Solve it mathematically
Iterate over i from 1 to n incrementing by 10 each time:

Add (n/(i*10))*i to countr representing the repetition of groups of i sizes after each (i*10) interval.

Add min(max((n mod (i*10)) - i + 1 ,0),i) to countr representing the additional digits dependant on the digit in iith place as described in intuition.

C++
int countDigitOne(int n)
{
    int countr = 0;
    for (long long i = 1; i <= n; i *= 10) {
        long long divider = i * 10;
        countr += (n / divider) * i + min(max(n % divider - i + 1, 0LL), i);
    }
    return countr;
}

(Thats what I did.)
O(log10(n)), O(1)

"""
# better:
class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        divisor = 10
        while True:
            q, r1 = divmod(n, divisor)
            b, r2 = divmod(r1, (divisor // 10))
            if b > 1:
                incre = q * (divisor // 10) + divisor // 10
            elif b == 1:
                incre = q * (divisor // 10) + r2 + 1
            else:
                incre = (q - 1) * (divisor // 10) +  divisor // 10
            res += incre
            if q == 0:
                break
            divisor *= 10
        return res
