"""Find the Longest Increasing Subsequence in Circular manner


Given an array, the task is to find to LIS (Longest Increasing Subsequence) in a circular way.


Examples : 
    Input : arr[] = {5, 4, 3, 2, 1}
    Output : 2
    Although there is no LIS in a given array 
    but in a circular form there can be
    {1, 5}, {2, 5}, ...... 

    Input : arr[]= {5, 6, 7, 1, 2, 3}
    Output : 6
    {1, 2, 3, 5, 6, 7} will be the LIS in the
    circular manner.
    

Append the same elements(i.e. whole array) with the given array.
For every window of size n(no. of elements in the given array), perform LIS.
Return maximum length.    



For example : Given array is {1, 4, 6, 2, 3}

After appending elements resultant array
will be {1, 4, 6, 2, 3, 1, 4, 6, 2, 3}.

Now for every consecutive n elements perform LIS.
1- {1, 4, 6, 2, 3} --3 is length of LIS.
2- {4, 6, 2, 3, 1} --2 is length of LIS.
3- {6, 2, 3, 1, 4} --3
4- {2, 3, 1, 4, 6}-- 4 {2, 3, 4, 6}
5- {3, 1, 4, 6, 2} --3.
6- {1, 4, 6, 2, 3} Original list.

So, maximum length of LIS in circular manner is 4. 
As in the last window we will have the same elements as in the given array which we don’t need to compute again, 
so we can append only n-1 elements to reduce the number of operations. 

"""





# Python3 implementation to find
# LIS in circular way Utility
# function to find LIS using
# Dynamic programmi
def computeLIS(circBuff, start, end, n):
	LIS = [0 for i in range(end)]
	
	# Initialize LIS values
	# for all indexes
	for i in range(start, end):
		LIS[i] = 1
		
	# Compute optimized LIS values
	# in bottom up manner
	for i in range(start + 1, end):
		
		# Set j on the basis of current
		# window i.e. first element of
		# the current window
		for j in range(start,i):
			if (circBuff[i] > circBuff[j] and
				LIS[i] < LIS[j] + 1):
				LIS[i] = LIS[j] + 1
				
	# Pick maximum of all LIS values
	res = -100000
	for i in range(start, end):
		res = max(res, LIS[i])
	return res

# Function to find Longest Increasing
# subsequence in Circular manner
def LICS(arr, n):
	
	# Make a copy of given
	# array by appending same
	# array elements to itself
	circBuff = [0 for i in range(2 * n)]
	for i in range(n):
		circBuff[i] = arr[i]
	for i in range(n, 2 * n):
		circBuff[i] = arr[i - n]
		
	# Perform LIS for each
	# window of size n
	res = -100000
	for i in range(n):
		res = max(computeLIS(circBuff, i,
							i + n, n), res)
	return res

# Driver code
arr = [ 1, 4, 6, 2, 3 ]
n = len(arr)
print("Length of LICS is", LICS(arr, n))


# Length of LICS is 4
# Time complexity of above solution is O(n3). It can be reduced O(n2 Log n) using O(n Log n) algorithm to find LIS.
