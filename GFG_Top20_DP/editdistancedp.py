"""Edit Distance
Given two strings str1 and str2 and below operations that can performed on str1. 
Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.  

Insert
Remove
Replace

say, m=Len(str1), n=Len(str2)
If last chars are same, nothing much to do. Ignore last characters and get count for remaining strings.

Else (If last characters are not same),
we consider all operations on ‘str1’, consider all three operations on last character of first string, 
recursively compute minimum cost for all three operations and take minimum of three values.

Insert: Recur for m and n-1
Remove: Recur for m-1 and n
Replace: Recur for m-1 and n-1

"""


# Recursion:
def editDistance(str1, str2, m, n):
	# If str1 is empty insert all chars of str2 into str1
	if m == 0:
		return n

	# If str2 is empty remove all characters of first string
	if n == 0:
		return m

	if str1[m-1] == str2[n-1]:
		return editDistance(str1, str2, m-1, n-1)

	# If last characters are not same, consider all three
	# operations on last character of first string, recursively
	# compute minimum cost for all three operations and take
	# minimum of three values.
	return 1 + min(editDistance(str1, str2, m, n-1), # Insert
				   editDistance(str1, str2, m-1, n), # Remove
				   editDistance(str1, str2, m-1, n-1) # Replace
				  )


# Driver code
str1 = "sunday"
str2 = "saturday"
print(editDistance(str1, str2, len(str1), len(str2)))

#simple but O(3^m) in the worst case

# -------------------------------------------------------------------------------------------------------


def editDistDP(str1, str2, m, n):
	# Create a table to store results of subproblems
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # BOTTOM ToP
	for i in range(m + 1):
		for j in range(n + 1):
	
            # If str1 is empty insert all chars of str2 into str1
			if i == 0:
				dp[i][j] = j # Min. operations = j

            # If str2 is empty remove all characters of first string
			elif j == 0:
				dp[i][j] = i # Min. operations = i

			# If last characters are same, ignore last char
			# and recur for remaining string
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]

			# If last character are different, consider all
			# possibilities and find minimum
			else:
				dp[i][j] = 1 + min(dp[i][j-1],	 # Insert
					    		   dp[i-1][j],	 # Remove
								   dp[i-1][j-1]) # Replace

	return dp[m][n]


# Driver code
str1 = "sunday"
str2 = "saturday"

print(editDistDP(str1, str2, len(str1), len(str2)))
"""
Time Complexity: O(m x n) 
Auxiliary Space: O(m x n)"""

# ----------------------------------------------------------------------------------------------------

#same program as above but space efficient

def EditDistDP(str1, str2):
	
	len1 = len(str1)
	len2 = len(str2)

	DP = [[0 for i in range(len1 + 1)] for j in range(2)]

	# Base condition when second String is empty then we remove all characters
	for i in range(0, len1 + 1):
		DP[0][i] = i

	# This loop run for every character in second String
	for i in range(1, len2 + 1):
		# This loop compares the char from second String with first String characters
		for j in range(0, len1 + 1):
			# If first String is empty then	we have to perform add character operation to get second String
			if (j == 0):
				DP[i % 2][j] = i

			# If character from both String is same then we do not perform any operation . 
            # here i % 2 is for bound the row number.

			elif(str1[j - 1] == str2[i-1]):
				DP[i % 2][j] = DP[(i - 1) % 2][j - 1]
			
			# If character from both String is not same then we take the minimum from three specified operation
			else:
				DP[i % 2][j] = (1 + min(DP[(i - 1) % 2][j],
									min(DP[i % 2][j - 1],
								DP[(i - 1) % 2][j - 1])))
			
	# After complete fill the DP array if the len2 is even then we end up in the 0th 
    # row else we end up in the 1th row so we take len2 % 2 to get row
	print(DP[len2 % 2][len1], "")

# Driver code
if __name__ == '__main__':
	
	str1 = "food"
	str2 = "money"
	
	EditDistDP(str1, str2)

"""
Time Complexity: O(m x n) 
Auxiliary Space: O( m )"""




# ----------------------------------------------------------------------------------------------------

# Memoizied top down APPROACH
def minDis(s1, s2, n, m, dp) :   
    
    if(n == 0) :
        return m       
    if(m == 0) :
        return n
                    
  # To check if the recursive tree
  # for given n & m has already been executed
    if(dp[n][m] != -1)  :
        return dp[n][m];
                   
  # If characters are equal, execute
  # recursive function for n-1, m-1   
    if(s1[n - 1] == s2[m - 1]) :          
        if(dp[n - 1][m - 1] == -1) :
            dp[n][m] = minDis(s1, s2, n - 1, m - 1, dp)
            return dp[n][m]                  
        else :
            dp[n][m] = dp[n - 1][m - 1]
            return dp[n][m]
         
  # If characters are nt equal, we need to          
  # find the minimum cost out of all 3 operations.        
    else :           
        if(dp[n - 1][m] != -1) :  
            m1 = dp[n - 1][m]     
        
        else:
            m1 = minDis(s1, s2, n - 1, m, dp)
              
        if(dp[n][m - 1] != -1) :               
            m2 = dp[n][m - 1]           
        else :
            m2 = minDis(s1, s2, n, m - 1, dp)  
        
        if(dp[n - 1][m - 1] != -1) :   
            m3 = dp[n - 1][m - 1]   
        else :
            m3 = minDis(s1, s2, n - 1, m - 1, dp)
     
        dp[n][m] = 1 + min(m1, min(m2, m3))
        return dp[n][m]
        
# Driver code
str1 = "voldemort"
str2 = "dumbledore"
    
n = len(str1)
m = len(str2)
dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
              
print(minDis(str1, str2, n, m, dp))















# leetcode contest
# _________________________________________________________________________________________________--
"""
Given two words, word1 and word2.
find the minimum number of operations required to convert word1 to word2

1. insert
2. delete
3. replace

Dynamic Programming

testcase:
word1 = 'horse'
word2 = 'ros'
answer = 3
"""


# O(N^2) time and space both
def editdist(w1, w2):
    r,c = len(w1), len(w2)
    dp = [[0 for j in range(c+1)] for i in range(r+1)]
    # print(*dp)
    for i in range(r+1):
        for j in range(c+1):
            # if w1 is empty, insert all chars of w2 in w1
            if i == 0:
                dp[i][j] = j

            # if w2 is empty, remove all chars of w1 
            elif j==0:
                dp[i][j] = i

            #if both the chars are same, ignore.
            elif w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            #else look for min(insert, delete, replace)
            else:
                # dp[i][j] = 1+min(insert,     delete,     replace)
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

    return dp[-1][-1]

word1 = 'hrsasfj'
word2 = 'ros'
answer = editdist(word1, word2)
print(answer)