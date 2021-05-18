# 0 1
# T(n)= T(n-1) + T(n-2)

# RECURSION O(2^N)
# DP O(N)  # MEMOIZATION

'''
def fib(n):
        if n == 0 or n == 1:
                return n
        else:
                return fib(n-1) + fib(n-2)
'''

# Global list for all test cases -.-
FIBDP = [0,1]
def fib(n):
        # already computed for previous testcases
        # no need to compute again
        # memoize
        if n < len(FIBDP):
                return FIBDP[n]        
        else:
                for i in range(len(FIBDP),n+1):
                        last = FIBDP[-1]
                        secondlast = FIBDP[-2]
                        FIBDP.append(last+secondlast)
                return FIBDP[n]

t = int(input())
for i in range(t):
        N = int(input())
        print(fib(N))
        print(FIBDP)
