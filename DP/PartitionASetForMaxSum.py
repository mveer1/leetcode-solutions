"""Find maximum subset sum formed by partitioning any subset of array into 2 partitions with equal sum
Difficulty Level : Expert

Given an array A containing N elements. Partition any subset of this array into two disjoint subsets such that both the subsets have an identical sum. Obtain the maximum sum that can be obtained after partitioning.

Note: It is not necessary to partition the entire array, that is any element might not contribute to any of the partition.

Examples:

Input: A = [1, 2, 3, 6]
Output: 6
Explanation: We have two disjoint subsets {1, 2, 3} and {6}, which have the same sum = 6

Input: A = [1, 2, 3, 4, 5, 6]
Output: 10
Explanation: We have two disjoint subsets {2, 3, 5} and {4, 6}, which have the same sum = 10.



Input: A = [1, 2]
Output: 0
Explanation: No subset can be partitioned into 2 disjoint subsets with identical sum









Naive Approach:
The above problem can be solved by brute force method using recursion. All the elements have three possibilities. Either it will contribute to partition 1 or partition 2 or will not be included in any of the partitions. We will perform these three operations on each of the element and proceed to the next element in each recursive step.

Below is the implementation of the above approach:
"""


# Python3 implementation for the
# above mentioned recursive approach

# Function to find the maximum subset sum
def maxSum(p0, p1, a, pos, n) :

	if (pos == n) :
		if (p0 == p1) :
			return p0;
		else :
			return 0;
	
	# Ignore the current element
	ans = maxSum(p0, p1, a, pos + 1, n);

	# including element in partition 1
	ans = max(ans, maxSum(p0 + a[pos], p1, a, pos + 1, n));

	# including element in partition 2
	ans = max(ans, maxSum(p0, p1 + a[pos], a, pos + 1, n));
	
	return ans;

# Driver code
if __name__ == "__main__" :

	# size of the array
	n = 4;
	a = [ 1, 2, 3, 6 ];
	
	print(maxSum(0, 0, a, 0, n));
# Time Complexity: O(3^n)




# efficient aproach:


# Now we might encounter, the difference between the sums is negative, lying in the range [-sum, +sum], where the sum is a summation of all elements. The minimum and maximum ranges occurring when one of the subsets is empty and the other one has all the elements. Due to this, in the DP state, we have defined j as (sum – diff). Thus, j will range from [0, 2*sum].



# Python3 implementation for the above mentioned
# Dynamic Programming approach

# import numpy as np
import sys

INT_MIN = -(sys.maxsize - 1)

# Function to find the maximum subset sum
def maxSum(a, n) :

	# sum of all elements
	sum = 0;
	for i in range(n) :
		sum += a[i];

	limit = 2 * sum + 1;

	# bottom up lookup table;
	dp = np.zeros((n + 1,limit));

	# initialising dp table with INT_MIN
	# where, INT_MIN means no solution
	for i in range(n + 1) :
		for j in range(limit) :
			dp[i][j] = INT_MIN;

	# Case when diff is 0
	dp[0][sum] = 0;
	for i in range(1, n + 1) :
		for j in range(limit) :

			# Putting ith element in g0
			if ((j - a[i - 1]) >= 0 and dp[i - 1][j - a[i - 1]] != INT_MIN) :

				dp[i][j] = max(dp[i][j], dp[i - 1][j - a[i - 1]]
											+ a[i - 1]);

			# Putting ith element in g1
			if ((j + a[i - 1]) < limit and dp[i - 1][j + a[i - 1]] != INT_MIN) :

				dp[i][j] = max(dp[i][j], dp[i - 1][j + a[i - 1]]);

			# Ignoring ith element
			if (dp[i - 1][j] != INT_MIN) :

				dp[i][j] = max(dp[i][j], dp[i - 1][j]);
				
	return dp[n][sum];

# Driver code

if __name__ == "__main__" :

	n = 4;
	a = [ 1, 2, 3, 6 ];
	print(maxSum(a, n));


# Time Complexity: O(N*Sum), where Sum represents sum of all array elements.
# Auxiliary Space: O(N*Sum)
# \\























































# https://www.geeksforgeeks.org/partition-problem-dp-18/

# check if this is done.