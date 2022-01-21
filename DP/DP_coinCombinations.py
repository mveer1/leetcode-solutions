"""
n coins, each has a positive integer value
you have to make a desired sum x, you can use a single coin any times
return the number of ordered ways to find that out.
"""

"""
testcase:
s = {2,3,5}
sum = 9
output will be 3. 225, 333, 2223      and 522 not included, only ordered.
"""

"""
approach: 9 is desired, make tree where all cases are covered like, 2 is taken or not etc

dp(i,x)  valid ways to make x using c1,c2,...ci
dp(n,x)  is our answer
"""

def cc(A, sum):
    n = len(A)
    dp = [[None for l in range(sum+1)] for k in range(n+1)]
    print(*dp)
    print('-'*9)
    # mod = 10
    for i in range(1, n+1):
        print(i)
        res = 0
        while res<=n:
            if res == 0:
                print("free block")
                dp[i][res]=i
            else:
                print("error space", i, res)
                i1 = 0 if A[i] > res else dp[i][res-A[i]]
                i2 = 0 if i==1 else dp[i-1][res]
                dp[i][res] = (i1 + i2)
            res+=1
            print(*dp)
            print()
    return dp



# print(cc([2,3,5], 9))

s = [2,3,5]
sum = 9
def ans(s, sum):
    if sum==0: return True
    if sum<0: return False
    #using recursion
    count = 0
    for i in s:
        result = ans(s, sum-i)
        if result:
            count += 1
    return count


def ansmemo1(s, sum, memo={}):
    if sum in memo: return memo[sum]
    if sum==0: return 1
    if sum<0: return 0

    count = 0
    for i in s:
        rem = sum - i
        if ansmemo1(s, rem, memo):
            count+=1

    memo[sum] = count
    return count
    

# print(ans(s, sum))
# print(ans([1,2,3,4,5,6], 100))
# print(ansmemo1(s, sum))
print(ansmemo1([1,2,3,5,6], 9))
print(ansmemo1([2,3,5], 9))

