"""
    n = 4   p = {1, 2, 5, 6}
    m = 8   w = {2, 3, 4, 5}

answer x = {0, 1, 0, 1} or something like this
"""

"""IN DP we always find a recursive solution, 
then we find a way to memoize it, 
if futher possible, we try to find a bottom up appoarch
"""

p = [-1, 1, 2, 5, 6]
m = 8   
w = [-1, 2, 3, 4, 5]
#added a dummy variable at the start so that we have better indexing

def knapsack(n, C):   #n is pointer to the item where we are making our decision, C is capacity left
    #base case, n==0, C==0
    if n==0 or C==0:
        result = 0
    elif w[n]<C:     #current weight is larger, we cant put it there. so we move left.
        result = knapsack(n-1, C)
    else:            #if not then will try both cases, putting it there and not putting it there.
        tmp1 = knapsack(n-1, C)                         #not putting it there
        tmp2 = p[n] + knapsack(n-1, C-w[n])            #putting it there
        result = max(tmp1, tmp2)
    return result

# print(knapsack(4, m))
#NOW THIS IS O(2^n)
#there fore trying memoziation in here.




n = 4
DP = [[-1 for l in range(m+1)] for k in range(n+1)]

def opknapsack(n, C):   #n is pointer to the item where we are making our decision, C is capacity left
    #base case, n==0, C==0
    if DP[n][C]==-1:
        return DP[n][C]
    if n==0 or C==0:
        result = 0
    elif w[n]>C:     #current wait is larger, we cant put it there. so we move left.
        result = knapsack(n-1, C)
    else:            #if not then will try both cases, putting it there and not putting it there.
        tmp1 = knapsack(n-1, C)                         #not putting it there
        tmp2 = p[n] + knapsack(n-1, C-w[n])            #putting it there
        result = max(tmp1, tmp2)
    result = DP[n][C]
    return result

# print(opknapsack(n,m))







#iterative
val = [1, 2, 5, 6]
W = 8   
wt = [2, 3, 4, 5]
n = len(val)

DP = [[0 for x in range(W + 1)] for x in range(n + 1)]

def op2knapsack(W, wt, val, n):
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                DP[i][w] = 0
            elif wt[i-1] <= w:
                DP[i][w] = max(val[i-1] + DP[i-1][w-wt[i-1]], DP[i-1][w])
            else:
                DP[i][w] = DP[i-1][w]
    return DP


# f = op2knapsack(W, wt, val, n)
# for i in f:
#     print(i)





#again optimal code but from gfg, recursive

# We initialize the matrix with -1 at first.
DP = [[-1 for i in range(W + 1)] for j in range(n + 1)]
 
 
def knapsack(wt, val, W, n):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if DP[n][W] != -1:
        return DP[n][W]
 
    # choice diagram code
    if wt[n-1] <= W:
        DP[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        return DP[n][W]
        
    elif wt[n-1] > W:
        DP[n][W] = knapsack(wt, val, W, n-1)
        return DP[n][W]
 

print(knapsack(wt, val, W, n))

