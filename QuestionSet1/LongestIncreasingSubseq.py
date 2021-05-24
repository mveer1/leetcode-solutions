""" LIC (but neccesarily Continuous)                 Source: GFG

For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}. 
"""


# Method 1: Recursion.
"""
Let arr[0 to n-1] be the input array and L(i) be the length of the LIS ending at index i 
such that arr[i] is the last element of the LIS  #which is true when it need not be continuous

Therefore, L(i) can be recursively written as: 

L(i) = 1 + max(L(j))       where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1                 , if no such j exists.



Input  : arr[] = {3, 10, 2, 11}
f(i): Denotes LIS of subarray ending at index 'i'

(LIS(1)=1)

      f(4)  {f(4) = 1 + max(f(1), f(2), f(3))}
  /    |    \
f(1)  f(2)  f(3) {f(3) = 1, f(2) and f(1) are > f(3)}
       |      |  \
      f(1)  f(2)  f(1) {f(2) = 1 + max(f(1)}
              |
            f(1) {f(1) = 1}
"""


""" To make use of recursive calls, this function must return
 two things:
 1) Length of LIS ending with element arr[n-1]. We use
 max_ending_here for this purpose
 2) Overall maximum as the LIS may end with an element
 before arr[n-1] max_ref is used this purpose.
 The value of LIS of full array of size n is stored in
 *max_ref which is our final result """
 
# global variable to store the maximum
global maximum
  

def lis(arr):
    # to allow the access of global variable
    global maximum
    n = len(arr)
    maximum = 1

    # The function _lis() stores its result in maximum
    _lis(arr, n)
    return maximum

def _lis(arr, n):
 
    # to allow the access of global variable
    global maximum
 
    if n == 1:
        return 1
 
    # maxEndingHere is the length of LIS ending with arr[n-1]
    maxEndingHere = 1
 
    """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
       IF arr[n-1] is smaller than arr[n-1], and max ending with
       arr[n-1] needs to be updated, then update it"""

    for i in range(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
            maxEndingHere = res + 1
 
    maximum = max(maximum, maxEndingHere)
 
    return maxEndingHere

 
# Driver program to test the above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print("Length of lis is ", lis(arr))
 

# Exponential Time


# ---------------------------------------------------------------------------------------------------------
# Iteration-wise simulation : 

def lis(arr):
    n = len(arr)

    lis = [1]*n
 
    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
 
    maximum = 0
 
    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])
 
    return maximum

"""
Time Complexity: O(n^2). 
As nested loop is used.
Auxiliary Space: O(n). 
 
 
# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print "Length of lis is", lis(arr)
"""












# ----------------------------------------------------------------------------------------------------
"""
If we closely observe the problem then we can convert this problem to longest Common Subsequence Problem.
Firstly we will create another array of unique elements of original array and sort it.
Now the longest increasing subsequence of our array must be present as a subsequence in our sorted array. 
That’s why our problem is now reduced to finding the common subsequence between the two arrays."""


# Dynamic Programming Approach of Finding LIS by reducing the problem to longest common Subsequence
 
def lis(a):
    n=len(a)
    # Creating the sorted list
    b=sorted(list(set(a)))
    m=len(b)
     
     
    # Creating dp table for storing the answers of sub problems
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
     
    # Finding Longest common Subsequence of the two arrays
    for i in range(n+1):
             
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif a[i-1]==b[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]
     
# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is ", lis(arr))


"""
Complexity Analysis : O(n^2)
Space Complexity : O(n^2)
"""