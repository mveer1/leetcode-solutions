# A binomial coefficient C(n, k) can be defined as 
# the coefficient of x^k in the expansion of (1 + x)^n.

# C(n, k) = C(n-1, k)   +   C(n-1, k-1) 
# B(n, k) = k*B(n-1, k) +   B(n-1, k-1)        #this was bell numbers
# P(n, k) = P(n-1, k) + k* P(n-1, k-1)         #this was permutation coeff 

def c(n, k, memo={}):
    if (n, k) in memo:
        return memo[(n, k)]    
    if k==0:
        return 1
    if k==n:
        return 1

    a1 = c(n-1, k, memo)
    a2 = c(n-1, k-1, memo)
    memo[(n,k)] = a1 + a2
    return memo[(n, k)]

print(c(100, 5))


def c_dp(n, k):
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n+1):
        for j in range(k+1):
            if i==j:
                dp[i][j] = 1
            elif j==0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
            # dp[i][j] = 
    return dp[n][k]

print(c_dp(100,5))