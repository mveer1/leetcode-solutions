# 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862
"""Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
Count the number of possible Binary Search Trees with n keys (See this)
Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect."""

# Cn+1 = sumation of Ci*C(n-i)  for i=0 to n for n>0

from time import time


def catalan(n, memo={}):
    if n in memo:
        return memo[n]
    if n==0 or n==1:
        return 1
    else:
        memo[n] = 0
        for i in range(n):
            a1 = catalan(i, memo)
            a2 = catalan(n-i-1, memo)
            memo[n] += a1*a2
        return memo[n]

a = time()
[catalan(i) for i in range(10)] 
b = time()
print(b-a)


