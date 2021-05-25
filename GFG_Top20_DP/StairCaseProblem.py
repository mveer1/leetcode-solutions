"""
Summary:
Question: Climbing a StairCase, cover n steps, by 1 or 2 at a time.
Return the number of ways to do that.

Approach 1: Fibonacci. (both iterative and recursive given below)
Approach 2: Recursion with memoization O(n)
Approach 3: Dynamic Programming  O(n)
Approach 4: Fibonacci but with space O(1)
Approach 5: Binets method (uses matrix mult to find fibo num)
Approach 6: Fibonacci formula, using sqrt(5) not accurate for higher values, 
"""




# mysolution
import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
class Solution:
    def climbStairs(self, n: int) -> int:
        i=2
        res=0
        while( n-2*i >= 0):
            res+= nCr(n-i, i) # (n-i) C (i)
            i+=1
        return int(n+res)

"""# brute force 2^n
public class Solution {
    public int climbStairs(int n) {
        return climb_Stairs(0, n);
    }
    public int climb_Stairs(int i, int n) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        return climb_Stairs(i + 1, n) + climb_Stairs(i + 2, n);
    }
}





# Approach 2: Recursion with Memoization  (O(n)) 
public class Solution {
    public int climbStairs(int n) {
        int memo[] = new int[n + 1];
        return climb_Stairs(0, n, memo);
    }
    public int climb_Stairs(int i, int n, int memo[]) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        if (memo[i] > 0) {
            return memo[i];
        }
        memo[i] = climb_Stairs(i + 1, n, memo) + climb_Stairs(i + 2, n, memo);
        return memo[i];
    }
}



# Approach 3: Dynamic Programming    (O(n))
One can reach ith step in one of the two ways:
   1. Taking a single step from (i−1)th step.

   2. Taking a step of 2 from (i-2)th step.

public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        return dp[n];
    }
}




Approach 4: Fibonacci Number  O(n) but space is O(1)
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) {
            return 1;
        }
        int first = 1;
        int second = 2;
        for (int i = 3; i <= n; i++) {
            int third = first + second;
            first = second;
            second = third;
        }
        return second;
    }
}
"""



"""
approach 5: Binets Method  time O(logn) and space constt
This is an interesting solution which uses matrix multiplication to obtain the nth Fibonacci Number. 
"""
# python: 
class Solution(object): 
    def climbStairs(self, n):
        q = [[1, 1], [1, 0]]
        res = self.matPow(q, n)
        return res[0][0]
  
    def matPow(self, a, n):
        ret = [[1, 0], [0, 1]]
        while n:
            if n & 1 == 1:
                ret = self.matMult(ret, a)
            n = n >> 1
            a = self.matMult(a, a)
        return ret
      
    def matMult(self, a, b):
        c = [[0 for x in range(2)] for z in range(2)]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c


# Approach 6: Fibonacci Formula O(logn), O(1)

n=1
# python: 
import math
sqrt5=math.sqrt(5)
fibn=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
# return int(fibn/sqrt5)


# =======================================================================================================================

# Similar Question
# Count number of ways to cover a distance
"""
Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps. 
"""

def printCountRec(dist):
    if dist < 0:
        return 0         
    if dist == 0:
        return 1
    return (printCountRec(dist-1) +
            printCountRec(dist-2) +
            printCountRec(dist-3))

dist = 4
print(printCountRec(dist))

# (horrible space and time O(3^n))

# efficient Aproach, using dp

def printCountDP(dist):
	count = [0] * (dist + 1)

	count[0] = 1
	if dist >= 1 :
		count[1] = 1
	if dist >= 2 :
		count[2] = 2
	
    # Bottom TOp
	for i in range(3, dist + 1):
		count[i] = (count[i-1] +
				count[i-2] + count[i-3])
		
	return count[dist];

dist = 4
print( printCountDP(dist))





"""
More Optimal Solution

Approach: Instead of using array of size n+1 we can use array of size 3 because for calculating 
no of ways for a particular step we need only last 3 steps no of ways.

Algorithm:
Create an array of size 3 and initialize the values for step 0,1,2 as 1,1,2 (Base cases).
Run a loop from 3 to n(dist).

For each index compute the value as ways[i%3] = ways[(i-1)%3] + ways[(i-2)%3] + ways[(i-3)%3] 
and store its value at i%3 index of array ways.

If we are computing value for index 3 then the computed value will go at index 0 because for larger
indices(4 ,5,6…..) we don’t need the value of index 0.
Return the value of ways[n%3].
"""

# In C++:
"""// A Dynamic Programming based C++ program to count number of ways
#include<iostream>
using namespace std;

int printCountDP(int dist)
{
		//Create the array of size 3.
		int ways[3] , n = dist;
		
		//Initialize the bases cases
		ways[0] = 1;
		ways[1] = 1;
		ways[2] = 2;
		
		//Run a loop from 3 to n
		//Bottom up approach to fill the array
		for(int i=3 ;i<=n ;i++)
			ways[i%3] = ways[(i-1)%3] + ways[(i-2)%3] + ways[(i-3)%3];
		
		return ways[n%3];
}

// driver program
int main()
{
	int dist = 4;
	cout << printCountDP(dist);
	return 0;
}


Time Complexity : O(n)
Space Complexity : O(1)"""





"""Approach: In previous article, a recursive and dynamic programming based approach has been discussed.
Here we will reduce the space complexity.
It can be onserved that to calculate the number of steps to cover the distance i, 
only the last three states are required (i – 1, i – 2, i – 3). So, the result can be calculated using the last three states.
"""
def countWays(n):
	
	# Base conditions
	if (n == 0):
		return 1
	if (n <= 2):
		return n

	# To store the last three stages
	f0 = 1
	f1 = 1
	f2 = 2
	ans = 0

	# Find the numbers of steps required
	# to reach the distance i
	for i in range(3, n + 1):
		ans = f0 + f1 + f2
		f0 = f1
		f1 = f2
		f2 = ans

	# Return the required answer
	return ans

# Driver code
n = 4

print(countWays(n))

# O(n)  time 
# O(1)  space






# from leetcode_Contests
"""
Staircase problem (via dp) 
1. 2 steps staircase problem
2. 3 steps staircase problem

Base case is taken where there exists only one way to take zero steps is to take no steps
"""

"""
**2 STEPS PROBLEM
1 step or 2 steps at a time
return the number of ways in which you can reach N steps.
ans(n) -> r
ans(0),ans(1) -> 1
ans(2) -> 2
ans = [1,1,2]
"""


"""
3 STEPS PROBLEM
you can take 1 step/2steps/3steps at a time
return the number of ways in which you can reach N steps.
ans(n) -> r
ans(0),ans(1) -> 1
ans(2) -> 2
ans(3) = 111 or 12 or 21 or 3  -> 4
[1,1,2,4]
"""


def countways2steps(n):
    dp = [0]*(n+1)
    dp[0], dp[1], dp[2] = 1,1,2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[-1]


def countways3steps(n):
    dp = [0]*(n+1)
    dp[0], dp[1], dp[2], dp[3] = 1,1,2,4
    for i in range(4, n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    return dp[-1]