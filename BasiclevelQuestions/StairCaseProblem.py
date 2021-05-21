"""
Staircase problem (via dp) 
1. 2 steps staircase problem
2. 3 steps staircase problem

Base case is taken where there exists only one way to take zero steps is to take no steps
"""

"""
**2 STEPS PROBLEM
1 step or 2 steps at a time
return the number of ways in which you can reach N steps.
ans(n) -> r
ans(0),ans(1) -> 1
ans(2) -> 2
ans = [1,1,2]
"""


"""
3 STEPS PROBLEM
you can take 1 step/2steps/3steps at a time
return the number of ways in which you can reach N steps.
ans(n) -> r
ans(0),ans(1) -> 1
ans(2) -> 2
ans(3) = 111 or 12 or 21 or 3  -> 4
[1,1,2,4]
"""


def countways2steps(n):
    dp = [0]*(n+1)
    dp[0], dp[1], dp[2] = 1,1,2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[-1]


def countways3steps(n):
    dp = [0]*(n+1)
    dp[0], dp[1], dp[2], dp[3] = 1,1,2,4
    for i in range(4, n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    return dp[-1]

