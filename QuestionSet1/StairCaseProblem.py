"""You are *climbing a staircase*. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
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

# brute force 2^n
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



approach 5: Binets Method  time O(logn) and space constt
This is an interesting solution which uses matrix multiplication to obtain the nth Fibonacci Number. 

python: 
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

java, official solution 
 public class Solution {
    public int climbStairs(int n) {
        int[][] q = {{1, 1}, {1, 0}};
        int[][] res = pow(q, n);
        return res[0][0];
    }
    public int[][] pow(int[][] a, int n) {
        int[][] ret = {{1, 0}, {0, 1}};
        while (n > 0) {
            if ((n & 1) == 1) {
                ret = multiply(ret, a);
            }
            n >>= 1;
            a = multiply(a, a);
        }
        return ret;
    }
    public int[][] multiply(int[][] a, int[][] b) {
        int[][] c = new int[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j];
            }
        }
        return c;
    }
}



Approach 6: Fibonacci Formula O(logn), O(1)

public class Solution {
    public int climbStairs(int n) {
        double sqrt5=Math.sqrt(5);
        double fibn=Math.pow((1+sqrt5)/2,n+1)-Math.pow((1-sqrt5)/2,n+1);
        return (int)(fibn/sqrt5);
    }
}

# python: 
import math
sqrt5=math.sqrt(5)
fibn=math.pow((1+sqrt5)/2,n+1)-math.pow((1-sqrt5)/2,n+1)
return int(fibn/sqrt5)