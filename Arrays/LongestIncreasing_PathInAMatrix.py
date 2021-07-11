"""Longest Increasing Path in Matrix

Problem Statement:
    Given a matrix of N rows and M columns. From m[i][j], 
      we can move to m[i+1][j], if m[i+1][j] > m[i][j], 
      or can move to m[i][j+1] if m[i][j+1] > m[i][j]. 
    The task is print longest path length if we start from (0, 0).

Example:
    Input : N = 4, M = 4
            m[][] = { { 1, 2, 3, 4 },
                      { 2, 2, 3, 4 },
                      { 3, 2, 3, 4 },
                      { 4, 5, 6, 7 } };
    Output : 7
    Longest path is 1 2 3 4 5 6 7.

    Input : N = 2, M =2
            m[][] = { { 1, 2 },
                      { 3, 4 } };
    Output :3
    Longest path is either 1 2 4 or 1 3 4

Aproach:
    The idea is to use dynamic programming. 
    Maintain the 2D matrix, dp[][], where dp[i][j] store the value of length of 
    longest increasing sequence for sub matrix starting from ith row and j-th column.

    Let the longest increasing sub sequence values for m[i+1][j] and m[i][j+1] be known already as v1 and v2 respectively. 
    Then the value for m[i][j] will be max(v1, v2) + 1.
    
    We can start from m[n-1][m-1] as base case with length of longest increasing sub sequence be 1, 
    moving upwards and leftwards updating the value of cells. Then the LIP value for cell m[0][0] will be the answer.

"""



# Python3 program to find longest
# increasing path in a matrix.
MAX = 20

# Return the length of
# LIP in 2D matrix
def LIP(dp, mat, n, m, x, y):
	
	# If value not calculated yet.
	if (dp[x][y] < 0):
		result = 0
		
		# If reach bottom left cell,
		# return 1.
		if (x == n - 1 and y == m - 1):
			dp[x][y] = 1
			return dp[x][y]

		# If reach the corner
		# of the matrix.
		if (x == n - 1 or y == m - 1):
			result = 1

		# If value greater than below cell.
		if (x + 1 < n and mat[x][y] < mat[x + 1][y]):
			result = 1 + LIP(dp, mat, n,
							m, x + 1, y)

		# If value greater than left cell.
		if (y + 1 < m and mat[x][y] < mat[x][y + 1]):
			result = max(result, 1 + LIP(dp, mat, n,
										m, x, y + 1))
		dp[x][y] = result
	return dp[x][y]

# Wrapper function
def wrapper(mat, n, m):
	dp = [[-1 for i in range(MAX)]
			for i in range(MAX)]
	return LIP(dp, mat, n, m, 0, 0)

# Driver Code
mat = [[1, 2, 3, 4 ],
	   [2, 2, 3, 4 ],
	   [3, 2, 3, 4 ],
	   [4, 5, 6, 7 ]]
n = 4
m = 4
print(wrapper(mat, n, m))


# Output:
# 7
# Time Complexity: O(N*M).