
#Is n (>0) power of 2
def ispowerof2(n):
    return n and not(n & (n-1))


# return's number of 1's in binary representation of int
# O(N)
def bruteforcecntbits(n):
    return str(bin(n))[2:].count('1')

# O(logn)
def cntbits(n):
    cnt = 0
    while n:
        cnt+=1
        n = n & (n-1)
        return cnt