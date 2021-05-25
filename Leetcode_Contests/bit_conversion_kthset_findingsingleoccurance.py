# n convert it into binary
def intToBin(n):
    return str(bin(n))[2:]

# bin to int 
def binToInt(s):
    return int(s,2)

# kth bit set from right
def kthbit(n,k):
    print(str(bin(n))[2:])
    if n & (1 << (k-1)):
        print("SET")
    else:
        print("NOT SET")


# n^n = 0
# n^0 = n
def findsingleoccur(arr):
    res = arr[0]
    for i in range(1,len(arr)):
        res = res ^ arr[i]
    return res
