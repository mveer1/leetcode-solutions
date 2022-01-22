# Given a set of n elements, find number of ways of partitioning it
# {1,2,3}

# 1 2 3
# 12 3
# 13 2
# 23 1
# 123 

# so 5
from time import time 

# B(n, 0) = 1
# B(n+1, k) = k*B(n, k) + B(n, k-1)

def S(n, k):                #called stirling numbers of second kind
    if k == 0 or k==1:  return 1
    if n == 0 or n == 1: return 0
    # if n == 1:  return 1
    
    # S(n, k) = k*S(n-1, k) + S(n-1, k-1)
    return k*S(n-1, k) + S(n-1, k-1)

def bell(n):
    res = 0
    for k in range(1,n+1):
        res += S(n, k)
    return res

# a = time()
# print(bell(20))
# b = time()
# print(b-a)

def printa(a):
    for i in range(len(a)):
        print(a[i])
    print()

def bellNumber(n):
    dp = [[0]*(n+1) for i in range(n+1)]
    dp[0][0] = 1

    for i in range(1, n+1): 
        # Explicitly fill for k = 0
        printa(dp)
        dp[i][0] = dp[i-1][i-1]
        # Fill for remaining values of j
        for k in range(1, i+1):
            printa(dp)
            dp[i][k] = dp[i-1][k-1] + dp[i][k-1]
    printa(dp)
    return dp[n][0]

a = time()
print(bellNumber(3))
b = time()
print(b-a)

