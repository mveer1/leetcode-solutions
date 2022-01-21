"""
Given a set of non-negative integers, and a value sum, determine 
if there is a subset of the given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
"""
Method 1: Recursion.
Approach: For the recursive approach we will consider two cases. 

Consider the last element and now the required sum = target sum – value of ‘last’ element and number of elements = total elements – 1
Leave the ‘last’ element and now the required sum = target sum and number of elements = total elements – 1

isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum) || isSubsetSum(set, n-1, sum-set[n-1])

Base Cases:
isSubsetSum(set, n, sum) = false, if sum > 0 and n == 0
isSubsetSum(set, n, sum) = true, if sum == 0 


example:
set[]={3, 4, 5, 2}
sum=9
(x, y)= 'x' is the left number of elements,
'y' is the required sum
  
              (4, 9)
             {True}
           /        \  
        (3, 6)       (3, 9)
               
        /    \        /   \ 
     (2, 2)  (2, 6)   (2, 5)  (2, 9)
     {True}  
     /   \ 
  (1, -3) (1, 2)  
{False}  {True} 
         /    \
       (0, 0)  (0, 2)
       {True} {False}      

"""

# A recursive solution for subset sum
# problem

# Returns true if there is a subset
# of set[] with sun equal to given sum


def isSubsetSum(set, n, sum):

	# Base Cases
	if (sum == 0):
		return True
	if (n == 0):
		return False

	# If last element is greater than
	# sum, then ignore it
	if (set[n - 1] > sum):
		return isSubsetSum(set, n - 1, sum)

	# else, check if sum can be obtained
	# by any of the following
	# (a) including the last element
	# (b) excluding the last element
	return isSubsetSum(
		set, n-1, sum) or isSubsetSum(
		set, n-1, sum-set[n-1])


# Driver code
set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
if (isSubsetSum(set, n, sum) == True):
	print("Found a subset with given sum")
else:
	print("No subset with given sum")

"""Output
Found a subset with given sum
Complexity Analysis: The above solution may try all subsets of given set in worst case. 
Therefore time complexity of the above solution is exponential. 
The problem is in-fact NP-Complete (There is no known polynomial time solution for this problem)."""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
"""
Method 2: To solve the problem in Pseudo-polynomial time use the Dynamic programming.
So we will create a 2D array of size (arr.size() + 1) * (target + 1) of type boolean. 
The state DP[i][j] will be true if there exists a subset of elements from A[0….i] 
with sum value = ‘j’. The approach for the problem is: 
if (A[i-1] > j)
    DP[i][j] = DP[i-1][j]
else 
    DP[i][j] = DP[i-1][j] OR DP[i-1][j-A[i-1]]

This means that if current element has value greater than ‘current sum value’ we will copy the answer for previous cases
And if the current sum value is greater than the ‘ith’ element we will see if any of 
previous states have already experienced the sum=’j’ OR any previous states experienced a value ‘j – A[i]’ which will solve our purpose.
The below simulation will clarify the above approach: 

set[]={3, 4, 5, 2}
target=6
 
    0    1    2    3    4    5    6

0   T    F    F    F    F    F    F

3   T    F    F    T    F    F    F
     
4   T    F    F    T    T    F    F   
      
5   T    F    F    T    T    T    F

2   T    F    T    T    T    T    T

"""

# A Dynamic Programming solution for subset
# sum problem Returns true if there is a subset of
# set[] with sun equal to given sum

# Returns true if there is a subset of set[]
# with sun equal to given sum
def isSubsetSum(set, n, sum):
	
	# The value of subset[i][j] will be
	# true if there is a
	# subset of set[0..j-1] with sum equal to i
	subset =([[False for i in range(sum + 1)]
			for i in range(n + 1)])
	
	# If sum is 0, then answer is true
	for i in range(n + 1):
		subset[i][0] = True
		
	# If sum is not 0 and set is empty,
	# then answer is false
	for i in range(1, sum + 1):
		subset[0][i]= False
			
	# Fill the subset table in botton up manner
	for i in range(1, n + 1):
		for j in range(1, sum + 1):
			if j<set[i-1]:
				subset[i][j] = subset[i-1][j]
			if j>= set[i-1]:
				subset[i][j] = (subset[i-1][j] or
								subset[i - 1][j-set[i-1]])
	
	# uncomment this code to print table
	# for i in range(n + 1):
	# for j in range(sum + 1):
	# print (subset[i][j], end =" ")
	# print()
	return subset[n][sum]
		
# Driver code
if __name__=='__main__':
	set = [3, 34, 4, 12, 5, 2]
	sum = 9
	n = len(set)
	if (isSubsetSum(set, n, sum) == True):
		print("Found a subset with given sum")
	else:
		print("No subset with given sum")
		
# Output
# Found a subset with given sum


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

"""
Memoization Technique for finding Subset Sum:

Method:

In this method, we also follow the recursive approach but In this method, 
we use another 2-D matrix in  we first initialize with -1 or any negative value.
In this method, we avoid the few of the recursive call which is repeated itself that’s why we use 2-D matrix. 
In this matrix we store the value of the previous call value.

Complexity Analysis: 

Time Complexity: O(sum*n), where sum is the ‘target sum’ and ‘n’ is the size of array.
Auxiliary Space: O(sum*n), as the size of 2-D array is sum*n.

"""

# in C++

"""// CPP program for the above approach
#include <bits/stdc++.h>
using namespace std;

// Taking the matrix as globally
int tab[2000][2000];

// Check if possible subset with
// given sum is possible or not
int subsetSum(int a[], int n, int sum)
{
	
	// If the sum is zero it means
	// we got our expected sum
	if (sum == 0)
		return 1;
		
	if (n <= 0)
		return 0;

	// If the value is not -1 it means it
	// already call the function
	// with the same value.
	// it will save our from the repetation.
	if (tab[n - 1][sum] != -1)
		return tab[n - 1][sum];

	// if the value of a[n-1] is
	// greater than the sum.
	// we call for the next value
	if (a[n - 1] > sum)
		return tab[n - 1][sum] = subsetSum(a, n - 1, sum);
	else
	{
		
		// Here we do two calls because we
		// don't know which value is
		// full-fill our critaria
		// that's why we doing two calls
		return tab[n - 1][sum] = subsetSum(a, n - 1, sum) ||
					subsetSum(a, n - 1, sum - a[n - 1]);
	}
}

// Driver Code
int main()
{
	// Storing the value -1 to the matrix
	memset(tab, -1, sizeof(tab));
	int n = 5;
	int a[] = {1, 5, 3, 7, 4};
	int sum = 12;

	if (subsetSum(a, n, sum))
	{
		cout << "YES" << endl;
	}
	else
		cout << "NO" << endl;

	/* This Code is Contributed by Ankit Kumar*/
}
"""






# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

"""
The solution discussed above requires O(n * sum) space and O(n * sum) time. 
We can optimize space. We create a boolean 2D array subset[2][sum+1]. Using bottom up manner we can fill up this table. 
The idea behind using 2 in “subset[2][sum+1]” is that for filling a row only the values from previous row is required. 
So alternate rows are used either making the first one as current and second as previous or the first as previous and second as current.

"""

# Returns true if there exists a subset
# with given sum in arr[]

def isSubsetSum(arr, n, sum):
	
	# The value of subset[i%2][j] will be true
	# if there exists a subset of sum j in
	# arr[0, 1, ...., i-1]
	subset = [ [False for j in range(sum + 1)] for i in range(3) ]

	for i in range(n + 1):
		for j in range(sum + 1):
			# A subset with sum 0 is always possible
			if (j == 0):
				subset[i % 2][j] = True

			# If there exists no element no sum
			# is possible
			elif (i == 0):
				subset[i % 2][j] = False
			elif (arr[i - 1] <= j):
				subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1)
																			% 2][j]
			else:
				subset[i % 2][j] = subset[(i + 1) % 2][j]
				
	return subset[n % 2][sum]

# Driver code
arr = [ 6, 2, 5 ]
sum = 7
n = len(arr)
if (isSubsetSum(arr, n, sum) == True):
	print ("There exists a subset with given sum")
else:
	print ("No subset exists with given sum")
	
# This code is contributed by Sachin Bisht







# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=

"""Similar Question:
Subset with Sum divible by M
"""


# Python3 program to check if there is
# a subset with sum divisible by m.

# Returns true if there is a subset
# of arr[] with sum divisible by m
def modularSum(arr, n, m):

	if (n > m):
		return True

	# This array will keep track of all
	# the possible sum (after modulo m)
	# which can be made using subsets of arr[]
	# initialising boolean array with all false
	DP = [False for i in range(m)]

	# we'll loop through all the elements of arr[]
	for i in range(n):
	
		# anytime we encounter a sum divisible
		# by m, we are done
		if (DP[0]):
			return True

		# To store all the new encountered sum (after
		# modulo). It is used to make sure that arr[i]
		# is added only to those entries for which DP[j]
		# was true before current iteration.
		temp = [False for i in range(m)]

		# For each element of arr[], we loop through
		# all elements of DP table from 1 to m and
		# we add current element i. e., arr[i] to
		# all those elements which are true in DP
		# table
		for j in range(m):
		
			# if an element is true in DP table
			if (DP[j] == True):
			
				if (DP[(j + arr[i]) % m] == False):

					# We update it in temp and update
					# to DP once loop of j is over
					temp[(j + arr[i]) % m] = True
			
		# Updating all the elements of temp
		# to DP table since iteration over
		# j is over
		for j in range(m):
			if (temp[j]):
				DP[j] = True

		# Also since arr[i] is a single element
		# subset, arr[i]%m is one of the possible
		# sum
		DP[arr[i] % m] = True
	
	return DP[0]

# Driver code
arr = [1, 7]
n = len(arr)
m = 5
print("YES") if(modularSum(arr, n, m)) else print("NO")
# Time Complexity : O(m^2)
# Auxiliary Space : O(m)