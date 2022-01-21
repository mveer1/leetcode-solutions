"""
p = 'BATD'
q = 'ABACD'

answer = 'BAD'
"""

"""Recursive solution
REturning the lenght of the longest common subsequence

Case 1: 
    p and q end with same chars p0  and q0 respectively
    return 1+LCS(P1, Q1)         #1 says the subsequence will end with p0/q0 
        
        Consider the input strings “AGGTAB” and “GXTXAYB”. Last characters match for the strings. So length of LCS can be written as:
        L(“AGGTAB”, “GXTXAYB”) = 1 + L(“AGGTA”, “GXTXAY”)

Case 2:
    p and q do not end with same chars, p0 and q0 are not same.
    return max(LCS(P1,Q0), LCS(P0, Q1))
"""

def LCS(P,Q,n,m):              #1 indexing, n is len(p), m is len(q) for the first call.  pointers basically
    if n==0 or m==0:
        result = 0
    elif P[n-1] == Q[m-1]:
        result = 1+LCS(P, Q, n-1, m-1)                      #last chars are same
    else:
        tmp1 = LCS(P, Q, n-1, m)
        tmp2 = LCS(P, Q, n, m-1)
        result = max(tmp1, tmp2)
    return result



#now memoization
P = ''
Q = ''
n = len(P)
m = len(Q)
dp = [[-1 for l in range(n)] for k in range(m)]

def LCSdp(P, Q, n, m):

    if dp[n][m]!=-1:         #do we have the result already?
        return dp[n][m]

    if n==0 or m==0:
        result = 0
    
    elif P[n-1] == Q[m-1]:
        result = 1+LCS(P, Q, n-1, m-1)                      #last chars are same

    else:
        tmp1 = LCS(P, Q, n-1, m)
        tmp2 = LCS(P, Q, n, m-1)
        result = max(tmp1, tmp2)
    dp[n][m]=result
    return result




#Now Bottom UP Solution

"""
            m=0     m=1     m=2     m=3
    n=0     0       0       0       0
    n=1     0       1       1       1
    n=2     0       1       2       2
"""

""" FRom GFG:
LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them. 
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.
"""

def lcs(X , Y):
    m = len(X)
    n = len(Y)
  
    # declaring the array for storing the dp values
    L = [[-1 for i in range(n+1)] for j in range(m+1)]
  
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
  
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
    
# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))



# --------------------------------------------------------------------------------------------------------------------

# PRINTING THE LCS

# Returns length of LCS for X[0..m-1], Y[0..n-1] 
def lcsprint(X, Y, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
  
    # Following code is used to print LCS
    index = L[m][n]
 
    lcs = [""] * (index+1)
    lcs[index] = ""
  
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
  
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i-=1
            j-=1
            index-=1
  
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i-=1
        else:
            j-=1
  
    print("LCS of",X, "and", Y, "is", "".join(lcs)) 
  
# Driver program
X = "AGGTAB"
Y = "GXTXAYB"
m = len(X)
n = len(Y)
lcsprint(X, Y, m, n)
  