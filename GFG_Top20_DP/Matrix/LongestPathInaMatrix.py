""" Find the longest path in a matrix with given constraints 

Problem:
    Given a n*n matrix where all numbers are distinct, find the maximum length path (starting from any cell) 
    such that all cells along the path are in increasing order with a difference of 1. 

Contraints:
    We can move in 4 directions from a given cell (i, j), 
    i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the condition  (no Diagonals)
    that the adjacent cells have a difference of 1.

Example: 
    Input:  mat[][] = {{1, 2, 9}
                    {5, 3, 8}
                    {4, 6, 7}}
    Output: 4

    The longest path is 6-7-8-9.


Solution Aproach:
    The idea is simple, we calculate longest path beginning with every cell. 
    Once we have computed longest for all cells, we return maximum of all longest paths.

Below is Dynamic Programming based implementation that uses a lookup table dp[][] to check if a problem is already solved or not.
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==

# Python3 program to find the longest path in a matrix with given constraints
n = 3
# This Function Returns length of the longest path beginning with mat[i][j] This function mainly uses lookup table dp[n][n]
def findLongestFromACell(i, j, mat, dp):
	if (i<0 or i>= n or j<0 or j>= n):   #Invalid index
		return 0

	if (dp[i][j] != -1):      #This is the DP Crux
		return dp[i][j]

	x, y, z, w = -1, -1, -1, -1              	# To store the path lengths in all the four directions

	# Since all numbers are unique and in range from 1 to n * n, there is atmost one possible direction from any cell
	if (j<n-1 and ((mat[i][j] +1) == mat[i][j + 1])):       
		x = 1 + findLongestFromACell(i, j + 1, mat, dp)

	if (j>0 and (mat[i][j] +1 == mat[i][j-1])):
		y = 1 + findLongestFromACell(i, j-1, mat, dp)

	if (i>0 and (mat[i][j] +1 == mat[i-1][j])):
		z = 1 + findLongestFromACell(i-1, j, mat, dp)

	if (i<n-1 and (mat[i][j] +1 == mat[i + 1][j])):
		w = 1 + findLongestFromACell(i + 1, j, mat, dp)

	dp[i][j] = max(x, max(y, max(z, max(w, 1))))             # If none of the adjacent fours is one greater we will take 1,: otherwise we will pick maximum from all the four directions
	return dp[i][j]

# now using the above function for all cells
def finLongestOverAll(mat):
	result = 1 

	dp =[[-1 for i in range(n)]for i in range(n)]

	for i in range(n):
		for j in range(n):
			if (dp[i][j] == -1):
				findLongestFromACell(i, j, mat, dp)
			result = max(result, dp[i][j])        # Update result when needed
	return result

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==

mat = [[1, 2, 9],
	[5, 3, 8],
	[4, 6, 7]]
print("Length of the longest path is ", finLongestOverAll(mat))


# Output:
# Length of the longest path is 4

# Time complexity of the above solution is O(n2). 
# It may seem more at first look. If we take a closer look, we can notice that all values of dp[i][j] are computed only once.

