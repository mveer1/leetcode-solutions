"""
Reach n by throwing a dice and adding up the result. 
Return the number of ways you can do it, modulo (10^9)+7

e.g. 
n=3
ways - 111 or 12 or 21 or 3
tree  -

            "3"
        1    2    3
    1  2    1     0
1      0    0       
0


dp[i] = sum of number of ways of throwing a dice so that sum = i
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4]+dp[i-5]+dp[i-6]   #i should be larger than 6 or this negative conditions should be avoided
        dp[0] = 1

"""

mod = (10**9) * 7
def dice(n):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for x in range(1,7):
            if x>i: break
            dp[i] = dp[i] + dp[i-x]
    print(dp[n])


dice(4)