# The Permutation Coefficient represented by P(n, k) 
# is used to represent the number of ways to obtain an 
# ordered subset having k elements from a set of n elements.

# P(n, k) = P(n-1, k) + k* P(n-1, k-1) 
# P(n, k) = n!/(k!*(n-k)!)

def p(n, k):
    if k == 0:
        return 1
    if k > n:
        return 0
    # return p(n-1, k) + k*p(n-1, k-1)
    return p(n-1, k) + k*p(n-1, k-1)

print(p(10, 2)) # 90
print(p(10, 3)) # 720
print(p(10, 0)) # 1
print(p(10, 1)) # 10


def p_dp(n, k):
    dp = [[0]*(k+1) for i in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(min(i,k)+1):
            if j==0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + j*dp[i-1][j-1]

            if j<k:
                dp[i][j+1] = 0 

    return dp[n][k]

print()
print(p_dp(10, 2)) # 90
print(p_dp(10, 3)) # 720
print(p_dp(10, 0)) # 1
print(p_dp(10, 1)) # 10