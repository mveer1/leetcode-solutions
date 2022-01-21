"""Partition a set into two subsets such that the difference of subset sums is minimum"""




# A Recursive Brute Force Aproach
# O(2^n)

# Function to find the minimum sum
def findMinRec(arr, i, sumCalculated, sumTotal):
 
    # If we have reached last element. 
    # Sum of one subset is sumCalculated,
    # sum of other subset is sumTotal-sumCalculated.  
    # Return absolute difference of two sums.
    if (i == 0):
        return abs((sumTotal - sumCalculated) - sumCalculated)

    # For every item arr[i], we have two choices
    # (1) We do not include it first set
    # (2) We include it in first set

    # We return minimum of two choices
    return min(findMinRec(arr, i - 1,
                          sumCalculated+arr[i - 1],
                          sumTotal),
               findMinRec(arr, i - 1,
                          sumCalculated, sumTotal))
 

# Returns minimum possible difference between sums of two subsets
def findMin(arr,  n):

    sumTotal = 0
    for i in range(n):
        sumTotal += arr[i]

    # recursive function
    return findMinRec(arr, n, 0, sumTotal)

# Driver code
if __name__ == "__main__":
 
    arr = [3, 1, 4, 2, 2, 1]
    n = len(arr)
    print("The minimum difference"+"between two sets is ", findMin(arr, n))




# -------------------------------------------------------------------
"""
The task is to divide the set into two parts. 
We will consider the following factors for dividing it. 
Let 
  dp[n+1][sum+1] = {1 if some subset from 1st to i'th has a sum 
                      equal to j
                   0 otherwise}
    
    i ranges from {1..n}
    j ranges from {0..(sum of all elements)}  

So      
    dp[n+1][sum+1]  will be 1 if 
    1) The sum j is achieved including i'th item
    2) The sum j is achieved excluding i'th item.

Let sum of all the elements be S.  

To find Minimum sum difference, w have to find j such 
that Min{sum - j*2  : dp[n][j]  == 1 } 
    where j varies from 0 to sum/2

The idea is, sum of S1 is j and it should be closest
to sum/2, i.e., 2*j should be closest to sum.
"""


import sys
 
# Returns the minimum value of the
# difference of the two sets.
def findMin(a, n):     
    su = 0
    # Calculate sum of all elements
    su = sum(a)

    # Create an 2d list to store
    # results of subproblems
    dp = [[0 for i in range(su + 1)]
             for j in range(n + 1)]
 
    # Initialize first column as true.
    # 0 sum is possible
    # with all elements.
    for i in range(n + 1):
        dp[i][0] = True
         
    # Initialize top row, except dp[0][0],
    # as false. With 0 elements, no other
    # sum except 0 is possible
    for j in range(1, su + 1):
        dp[0][j] = False
     
    # Fill the partition table in
    # bottom up manner
    for i in range(1, n + 1):
        for j in range(1, su + 1):
             
            # If i'th element is excluded
            dp[i][j] = dp[i - 1][j]
             
            # If i'th element is included
            if a[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - a[i - 1]]
     
    # Initialize difference
    # of two sums.
    diff = sys.maxsize
 
    # Find the largest j such that dp[n][j]
    # is true where j loops from sum/2 t0 0
    for j in range(su // 2, -1, -1):
        if dp[n][j] == True:
            diff = su - (2 * j)
            break
             
    return diff
     
# Driver code
a = [ 3, 1, 4, 2, 2, 1 ]
n = len(a)
     
print("The minimum difference between 2 sets is ", findMin(a, n))



# Time Complexity = O(n*sum)
# Note that the above solution is in Pseudo Polynomial Time (time complexity is dependent on the numeric value of input).


# ---------------------------------------------------------------------
"""similar problem:
Partition problem | DP-18
Partition problem is to determine whether 
a given set can be partitioned into two subsets 
such that the sum of elements in both subsets is the same. 

Example: 

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

Following are the two main steps to solve this problem: 
1) Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return false. 
2) If sum of array elements is even, calculate sum/2 and find a subset of array with sum equal to sum/2. 
The first step is simple. The second step is crucial, it can be solved either using recursion or Dynamic Programming.




Let isSubsetSum(arr, n, sum/2) be the function that returns true if 
there is a subset of arr[0..n-1] with sum equal to sum/2

The isSubsetSum problem can be divided into two subproblems
 a) isSubsetSum() without considering last element 
    (reducing n to n-1)
 b) isSubsetSum considering the last element 
    (reducing sum/2 by arr[n-1] and n to n-1)
If any of the above the above subproblems return true, then return true. 
isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
                              isSubsetSum (arr, n-1, sum/2 - arr[n-1])


"""

# A utility function that returns true if there is a subset of arr[] with sun equal to given sum

def isSubsetSum(arr, n, sum):
    # Base Cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
 
    # If last element is greater than sum, then
    # ignore it
    if arr[n-1] > sum:
        return isSubsetSum(arr, n-1, sum)
 
    ''' else, check if sum can be obtained by any of
    the following
    (a) including the last element
    (b) excluding the last element'''
 
    return isSubsetSum(arr, n-1, sum) or isSubsetSum(arr, n-1, sum-arr[n-1])
 
# Returns true if arr[] can be partitioned in two
# subsets of equal sum, otherwise false
 
 
def findPartion(arr, n):
    # Calculate sum of the elements in array
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    # If sum is odd, there cannot be two subsets
    # with equal sum
    if sum % 2 != 0:
        return False
 
    # Find if there is subset with sum equal to
    # half of total sum
    return isSubsetSum(arr, n, sum // 2)
 
 
# Driver code
arr = [3, 1, 5, 9, 12]
n = len(arr)

# Function call
if findPartion(arr, n) == True:
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")

# Time Complexity: O(2^n)

# ------------------------------------------------------------------------------

def findPartition(arr, n):
    sum = 0
    i, j = 0, 0
 
    # calculate sum of all elements
    for i in range(n):
        sum += arr[i]
 
    if sum % 2 != 0:
        return False
 
    part = [[True for i in range(n + 1)]
            for j in range(sum // 2 + 1)]
 
    # initialize top row as true
    for i in range(0, n + 1):
        part[0][i] = True
 
    # initialize leftmost column,
    # except part[0][0], as 0
    for i in range(1, sum // 2 + 1):
        part[i][0] = False
 
    # fill the partition table in
    # bottom up manner
    for i in range(1, sum // 2 + 1):
 
        for j in range(1, n + 1):
            part[i][j] = part[i][j - 1]
 
            if i >= arr[j - 1]:
                part[i][j] = (part[i][j] or part[i - arr[j - 1]][j - 1])
 
    return part[sum // 2][n]
 
 
# Driver Code
arr = [3, 1, 1, 2, 2, 1]
n = len(arr)
 
# Function call
if findPartition(arr, n) == True:
    print("Can be divided into two", "subsets of equal sum")
else:
    print("Can not be divided into ","two subsets of equal sum")

"""
Time Complexity: O(sum*n) 
Auxiliary Space: O(sum*n) 

Please note that this solution will not be feasible for arrays with big sum."""

# -------------------------------------------------------------------------------------

# Returns true if arr[] can be partitioned in two subsets of equal sum, otherwise false
def findPartiion(arr, n) :
    Sum = 0
 
    # Calculate sum of all elements
    for i in range(n) :
        Sum += arr[i]
    if (Sum % 2 != 0) :
        return 0
    part = [0] * ((Sum // 2) + 1)
 
    # Initialze the part array as 0
    for i in range((Sum // 2) + 1) :
        part[i] = 0
 
    # Fill the partition table in bottom up manner
    for i in range(n) :
       
        # the element to be included
        # in the sum cannot be
        # greater than the sum
        for j in range(Sum // 2, arr[i] - 1, -1) :
           
            # check if sum - arr[i]
            # could be formed
            # from a subset
            # using elements
            # before index i
            if (part[j - arr[i]] == 1 or j == arr[i]) :
                part[j] = 1
 
    return part[Sum // 2]
 
# Drive code 
arr = [ 1, 3, 3, 2, 3, 2 ]
n = len(arr)
 
# Function call
if (findPartiion(arr, n) == 1) :
    print("Can be divided into two subsets of equal sum")
else :
    print("Can not be divided into two subsets of equal sum")
