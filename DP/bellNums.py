# Given a set of n elements, find number of ways of partitioning it


# Another problem that can be solved by Bell Numbers. 
# A number is squarefree if it is not divisible by a perfect square other than 1. For example, 6 is a square free number but 12 is not as it is divisible by 4. 
# Given a squarefree number x, find the number of different multiplicative partitions of x. 
# The number of multiplicative partitions is Bell(n) where n is number of prime factors of x. 
# For example x = 30, there are 3 prime factors of 2, 3 and 5. So the answer is Bell(3) which is 5. 
# The 5 partitions are 1 x 30, 2 x15, 3 x 10, 5 x 6 and 2 x 3 x 5.# {1,2,3}


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

