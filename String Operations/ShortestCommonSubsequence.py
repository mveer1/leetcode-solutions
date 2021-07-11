"""Shortest Common Supersequence
Difficulty Level : Medium
Last Updated : 12 May, 2021
Given two strings str1 and str2, the task is to find the length of the shortest string that has both str1 and str2 as subsequences.

Examples : 
Input:   str1 = "geek",  str2 = "eke"
Output: 5
Explanation: 
String "geeke" has both string "geek" 
and "eke" as subsequences.

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  9
Explanation: 
String "AGXGTXAYB" has both string 
"AGGTAB" and "GXTXAYB" as subsequences.


This problem is closely related to longest common subsequence problem. Below are steps.
1) Find Longest Common Subsequence (lcs) of two given strings. For example, lcs of “geek” and “eke” is “ek”. 
2) Insert non-lcs characters (in their original order in strings) to the lcs found above, and return the result. So “ek” becomes “geeke” which is shortest common supersequence.
Let us consider another example, str1 = “AGGTAB” and str2 = “GXTXAYB”. LCS of str1 and str2 is “GTAB”. Once we find LCS, we insert characters of both strings in order and we get “AGXGTXAYB”
How does this work? 
We need to find a string that has both strings as subsequences and is shortest such string. If both strings have all characters different, then result is sum of lengths of two given strings. If there are common characters, then we don’t want them multiple times as the task is to minimize length. Therefore, we fist find the longest common subsequence, take one occurrence of this subsequence and add extra characters. 


Length of the shortest supersequence  
= (Sum of lengths of given two strings) 
- (Length of LCS of two given strings) 
"""


# Python program to find length
# of the shortest supersequence

# Function to find length of the
# shortest supersequence of X and Y.


def shortestSuperSequence(X, Y):
	m = len(X)
	n = len(Y)
	l = lcs(X, Y, m, n)

	# Result is sum of input string
	# lengths - length of lcs
	return (m + n - l)

# Returns length of LCS for
# X[0..m - 1], Y[0..n - 1]


def lcs(X, Y, m, n):
	L = [[0] * (n + 2) for i in
		range(m + 2)]

	# Following steps build L[m + 1][n + 1]
	# in bottom up fashion. Note that L[i][j]
	# contains length of LCS of X[0..i - 1]
	# and Y[0..j - 1]
	for i in range(m + 1):

		for j in range(n + 1):

			if (i == 0 or j == 0):
				L[i][j] = 0

			elif (X[i - 1] == Y[j - 1]):
				L[i][j] = L[i - 1][j - 1] + 1

			else:
				L[i][j] = max(L[i - 1][j],
							L[i][j - 1])

	# L[m][n] contains length of
	# LCS for X[0..n - 1] and Y[0..m - 1]
	return L[m][n]


# Driver code
X = "AGGTAB"
Y = "GXTXAYB"

print("Length of the shortest supersequence is %d"
	% shortestSuperSequence(X, Y))



# _----------------------------------------------------------------------------------------------------------------


""""
Below is Another Method to solve the above problem. 
A simple analysis yields below simple recursive solution.

Let X[0..m - 1] and Y[0..n - 1] be two 
strings and m and n be respective
lengths.

  if (m == 0) return n;
  if (n == 0) return m;

  // If last characters are same, then 
  // add 1 to result and
  // recur for X[]
  if (X[m - 1] == Y[n - 1])
     return 1 + SCS(X, Y, m - 1, n - 1);

  // Else find shortest of following two
  //  a) Remove last character from X and recur
  //  b) Remove last character from Y and recur
  else 
    return 1 + min( SCS(X, Y, m - 1, n), SCS(X, Y, m, n - 1) );
Below is simple naive recursive solution based on above recursive formula. 
"""

# A Naive recursive python program to find
# length of the shortest supersequence
 
 
def superSeq(X, Y, m, n):
    if (not m):
        return n
    if (not n):
        return m
 
    if (X[m - 1] == Y[n - 1]):
        return 1 + superSeq(X, Y, m - 1, n - 1)
 
    return 1 + min(superSeq(X, Y, m - 1, n),
                   superSeq(X, Y, m, n - 1))
 
 
# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))


"""Time complexity of the above solution exponential O(2min(m, n)). 
Since there are overlapping subproblems, we can efficiently solve this recursive problem using Dynamic Programming. 


Below is Dynamic Programming based implementation. 
Time complexity of this solution is O(mn). 

"""


# A dynamic programming based python program
# to find length of the shortest supersequence

# Returns length of the shortest supersequence of X and Y


def superSeq(X, Y, m, n):
	dp = [[0] * (n + 2) for i in range(m + 2)]

	# Fill table in bottom up manner
	for i in range(m + 1):
		for j in range(n + 1):

			# Below steps follow above recurrence
			if (not i):
				dp[i][j] = j
			elif (not j):
				dp[i][j] = i

			elif (X[i - 1] == Y[j - 1]):
				dp[i][j] = 1 + dp[i - 1][j - 1]

			else:
				dp[i][j] = 1 + min(dp[i - 1][j],
								dp[i][j - 1])

	return dp[m][n]


# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of the shortest supersequence is %d"
	% superSeq(X, Y, len(X), len(Y)))





"""
Top Down Memoization Approach : 
The idea is to follow the simple recursive solution, use a lookup table to avoid recomputations. Before computing result for an input, we check if the result is already computed or not. If already computed, we return that result.

"""
# A dynamic programming based python program
# to find length of the shortest supersequence
 
# Returns length of the
# shortest supersequence of X and Y
 
# import numpy as np
def superSeq(X,Y,n,m,lookup):
     
    if m==0 or n==0:
        lookup[n][m] = n+m
 
    if (lookup[n][m] == 0):    
        if X[n-1]==Y[m-1]:
            lookup[n][m] = superSeq(X,Y,n-1,m-1,lookup)+1
     
        else:
            lookup[n][m] = min(superSeq(X,Y,n-1,m,lookup)+1,
                               superSeq(X,Y,n,m-1,lookup)+1)
     
    return lookup[n][m]
     
 
 
# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
 
lookup = np.zeros([len(X)+1,len(Y)+1])
print("Length of the shortest supersequence is {}"
      .format(superSeq(X,Y,len(X),len(Y),lookup)))
 
# This code is contributed by Tanmay Ambadkar
# Output: 

# Length of the shortest supersequence is 9.0





"""
Shortest possible combination of two strings
Difficulty Level : Hard
Last Updated : 10 Mar, 2021
Compute the shortest string for a combination of two given strings such that the new string consist of both the strings as its subsequences.
Examples: 
 

Input : a = "pear"
        b = "peach"
Output : pearch
pearch is the shorted string such that both
pear and peach are its subsequences.

Input  : a = "geek"
         b = "code"
Output : gecodek"""

"""
We have discussed a solution to find length of the shortest supersequence in below post. 
Shortest Common Supersequence
In this post, printing of supersequence is discussed. The solution is based on below recursive approach discussed in above post as an alternate method.
"""

"""
Let a[0..m-1] and b[0..n-1] be two strings and m and
be respective lengths.

  if (m == 0) return n;
  if (n == 0) return m;

  // If last characters are same, then add 1 to
  // result and recur for a[]
  if (a[m-1] == b[n-1]) 
     return 1 + SCS(a, b, m-1, n-1);

  // Else find shortest of following two
  //  a) Remove last character from X and recur
  //  b) Remove last character from Y and recur
  else return 1 + min( SCS(a, b, m-1, n), 
                       SCS(a, b, m, n-1) );
We build a DP array to store lengths. After building the DP array, we traverse from bottom right most position. The approach of printing is similar to printing LCS."""




# Python3 program to print supersequence of two strings

# Prints super sequence of a[0..m-1] and b[0..n-1]
def printSuperSeq(a, b):
	m = len(a)
	n = len(b)
	dp = [[0] * (n + 1) for i in range(m + 1)]

	# Fill table in bottom up manner
	for i in range(0, m + 1):
		for j in range(0, n + 1):
			
			# Below steps follow above recurrence
			if not i:
				dp[i][j] = j;
			elif not j:
				dp[i][j] = i;
			elif (a[i - 1] == b[j - 1]):
				dp[i][j] = 1 + dp[i - 1][j - 1];
			else:
				dp[i][j] = 1 + min(dp[i - 1][j],
								dp[i][j - 1]);

	# Following code is used to print supersequence
	index = dp[m][n];

	# Create a string of size index+1
	# to store the result
	res = [""] * (index)

	# Start from the right-most-bottom-most corner
	# and one by one store characters in res[]
	i = m
	j = n;
	while (i > 0 and j > 0):
	
		# If current character in a[] and b are same,
		# then current character is part of LCS
		if (a[i - 1] == b[j - 1]):
		
			# Put current character in result
			res[index - 1] = a[i - 1];

			# reduce values of i, j and indexs
			i -= 1
			j -= 1
			index -= 1
		
		# If not same, then find the larger of two and
		# go in the direction of larger value
		elif (dp[i - 1][j] < dp[i][j - 1]):
			res[index - 1] = a[i - 1]
			i -= 1
			index -= 1

		else:
			res[index - 1] = b[j - 1]
			j -= 1
			index -= 1

	# Copy remaining characters of string 'a'
	while (i > 0):
		res[index - 1] = a[i - 1]
		i -= 1
		index -= 1

	# Copy remaining characters of string 'b'
	while (j > 0):
		res[index - 1] = b[j - 1]
		j -= 1
		index -= 1

	# Print the result
	print("".join(res))

# Driver Code
if __name__ == '__main__':
	a = "algorithm"
	b = "rhythm"
	printSuperSeq(a, b)
	
# This code is contributed by ashutosh450






# We build the 2D array using LCS solution. If the character at the two pointer positions is equal, we increment the length by 1, else we store the minimum of the adjacent positions. Finally, we backtrack the matrix to find the index vector traversing which would yield the shortest possible combination. 
 


# Python implementation to find shortest string for
# a combination of two strings
index_a = []
index_b = []
 
def index(dp, a, b, size_a, size_b):
    if (size_a == 0 or size_b == 0):
        return
    if (a[size_a - 1] == b[size_b - 1]):
        index(dp, a, b, size_a - 1, size_b - 1)
        index_a.append(size_a - 1)
        index_b.append(size_b - 1)
    else:
        if(dp[size_a - 1][size_b] > dp[size_a][size_b - 1]):
            index(dp, a, b, size_a - 1, size_b)
        else:
            index(dp, a, b, size_a, size_b - 1)
     
def combine(a, b, size_a, size_b):
    dp = [[0 for i in range(100)] for j in range(100)]
    ans = ""
    k = 0
     
    for i in range(1, size_a + 1):
        for j in range(1, size_b + 1):
            if(a[i - 1] == b[j - 1]):
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
     
    lcs = dp[size_a][size_b]
    index(dp, a, b, size_a, size_b)
    j = i = k
    while (k < lcs):
        while (i < size_a and i < index_a[k]):
            ans += a[i];
            i += 1
        while (j < size_b and j < index_b[k]):
            ans += b[j]
            j += 1
        ans = ans + a[index_a[k]]
        k += 1
        i += 1
        j += 1
     
    while (i < size_a):
        ans += a[i]
        i += 1
    while (j < size_b):
        ans += b[j]
        j += 1
    print(ans)
 
# Driver code
a = "algorithm"
b = "rhythm"
size_a = len(a)
size_b = len(b)
combine(a, b, size_a, size_b)
 
# This code is contributed by avanitrachhadiya2155
# Output: 
 

# algorihythm


