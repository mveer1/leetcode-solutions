"""Longest Common Increasing Subsequence (LCS + LIS)
Difficulty Level : Hard

Given two arrays, find length of the longest common increasing subsequence [LCIS] and 
print one of such sequences (multiple sequences may exist)

arr1[] = {3, 4, 9, 1} and 
arr2[] = {5, 3, 8, 9, 10, 2, 1}
Our answer would be {3, 9} as this is the longest common subsequence which is increasing also.



The idea is to use dynamic programming here as well.
We store the longest common increasing sub-sequence ending at each index of arr2[]. 
We create an auxiliary array table[] such that table[j] stores length of LCIS ending with arr2[j]. 
At the end, we return maximum value from this table. 
For filling values in this table, we traverse all elements of arr1[] and for every element arr1[i], 
we traverse all elements of arr2[]. If we find a match, we update table[j] with length of current LCIS. 
To maintain current LCIS, we keep checking valid table[j] values.
Below is the program to find length of LCIS. 
"""

# Python 3 Program to find length of the
# Longest Common Increasing Subsequence (LCIS)

# Returns the length and the LCIS of two
# arrays arr1[0..n-1] and arr2[0..m-1]
def LCIS(arr1, n, arr2, m):

	# table[j] is going to store length of LCIS
	# ending with arr2[j]. We initialize it as 0,
	table = [0] * m
	for j in range(m):
		table[j] = 0

	# Traverse all elements of arr1[]
	for i in range(n):
	
		# Initialize current length of LCIS
		current = 0

		# For each element of arr1[],
		# traverse all elements of arr2[].
		for j in range(m):
			
			# If both the array have same elements.
			# Note that we don't break the loop here.
			if (arr1[i] == arr2[j]):
				if (current + 1 > table[j]):
					table[j] = current + 1

			# Now seek for previous smaller common
			# element for current element of arr1
			if (arr1[i] > arr2[j]):
				if (table[j] > current):
					current = table[j]

	# The maximum value in table[]
	# is out result
	result = 0
	for i in range(m):
		if (table[i] > result):
			result = table[i]

	return result

# Driver Code
if __name__ == "__main__":
	
	arr1 = [3, 4, 9, 1]
	arr2 = [5, 3, 8, 9, 10, 2, 1]

	n = len(arr1)
	m = len(arr2)

	print("Length of LCIS is",
		LCIS(arr1, n, arr2, m))


# output:
# Length of LCIS is 2