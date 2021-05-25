"""
BUY and SELL stock
max profit, buy before selling
[7,1,5,3,6,4]
buy on 1 and sell on 6
"""
A = [7,1,5,3,6,4, 100]

# O(N^2)
def bruteforce(A):
    n = len(A)
    maxprof = 0
    for i in range(n):   #buy
        for j in range(1+i, n):  #sell
            if A[j] > A[i]:
                maxprof = max(maxprof, A[j]-A[i])
    return maxprof


print(bruteforce(A))

# O(N)
def optimal(A):
    n = len(A)
    maxprof = 0
    minprice = float("inf")
    for i in range(n):
        minprice = min(minprice, A[i])  #
        maxprof = max(maxprof, A[i]-minprice)  #

    print(maxprof)

optimal(A)