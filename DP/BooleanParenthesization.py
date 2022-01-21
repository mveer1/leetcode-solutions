"""Boolean Parenthesization Problem | DP-37
Difficulty Level : Expert

Problem Statement:
    Count the number of ways we can parenthesize the expression so that 
    the value of expression evaluates to true.

Examples:

1.      Input: symbol[]    = {T, F, T}
            operator[]  = {^, &}
        Output: 2

        The given expression is "T ^ F & T", it evaluates true
        in two ways "((T ^ F) & T)" and "(T ^ (F & T))"

2.      Input: symbol[]    = {T, F, F}
            operator[]  = {^, |}
        Output: 2

        The given expression is "T ^ F | F", it evaluates true
        in two ways "( (T ^ F) | F )" and "( T ^ (F | F) )". 

3.      Input: symbol[]    = {T, T, F, T}
            operator[]  = {|, &, ^}
        Output: 4

        The given expression is "T | T & F ^ T", it evaluates true
        in 4 ways ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) 
        and (T|((T&F)^T)). 



Solution: 
Let T(i, j) represents the number of ways to parenthesize the 
symbols between i and j (both inclusive) such that the subexpression between i and j evaluates to true. 

Let F(i, j) represents the number of ways to parenthesize the 
symbols between i and j (both inclusive) such that the subexpression between i and j evaluates to false.

T(i,j) =  Sumation from k=1 to j-1
                    1. T(i,k) * T(k+1,j)                              if operator [k] is &
                    2. Total(i,k)*Total(k+1,j)  - F(i,k)*F(k+1,j)     if operator [k] is | 
                    3. T(i,k)*F(K+1,j) + F(i,k)*T(K+1,j)              if operator [k] is ^

F(i,j) = Sumation from k=1 to j-1
                    1. Total(i,k)*Total(k+1,j)  - T(i,k)*T(k+1,j)     if operator [k] is &
                    2. F(i,k)*F(k+1,j)                                if operator [k] is |
                    3. T(i,k) * T(k+1,j)  +  F(i,k) * F(k+1,j)        if operator [k] is ^

Total(i,j)= T(i,j)+F(i,j)


Base Cases:

T(i, i) = 1 if symbol[i] = 'T' 
T(i, i) = 0 if symbol[i] = 'F' 

F(i, i) = 1 if symbol[i] = 'F' 
F(i, i) = 0 if symbol[i] = 'T'
"""


# Returns count of all possible
# parenthesizations that lead to
# result true for a boolean
# expression with symbols like
# true and false and operators
# like &, | and ^ filled between symbols
 
 
def countParenth(symb, oper, n):
    F = [[0 for i in range(n + 1)]
            for i in range(n + 1)]
    
    T = [[0 for i in range(n + 1)]
            for i in range(n + 1)]
 
    # Fill diaginal entries first
    # All diagonal entries in
    # T[i][i] are 1 if symbol[i]
    # is T (true). Similarly, all
    # F[i][i] entries are 1 if
    # symbol[i] is F (False)
    for i in range(n):
        if symb[i] == 'F':
            F[i][i] = 1
        else:
            F[i][i] = 0
 
        if symb[i] == 'T':
            T[i][i] = 1
        else:
            T[i][i] = 0
 
    # Now fill T[i][i+1], T[i][i+2],
    # T[i][i+3]... in order And
    # F[i][i+1], F[i][i+2],
    # F[i][i+3]... in order
    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            T[i][j] = F[i][j] = 0
            for g in range(gap):
 
                # Find place of parenthesization
                # using current value of gap
                k = i + g
 
                # Store Total[i][k] and Total[k+1][j]
                tik = T[i][k] + F[i][k]
                tkj = T[k + 1][j] + F[k + 1][j]
 
                # Follow the recursive formulas
                # according to the current operator
                if oper[k] == '&':
                    T[i][j] += T[i][k] * T[k + 1][j]
                    F[i][j] += (tik * tkj - T[i][k] *
                                T[k + 1][j])
                if oper[k] == '|':
                    F[i][j] += F[i][k] * F[k + 1][j]
                    T[i][j] += (tik * tkj - F[i][k] *
                                F[k + 1][j])
                if oper[k] == '^':
                    T[i][j] += (F[i][k] * T[k + 1][j] +
                                T[i][k] * F[k + 1][j])
                    F[i][j] += (T[i][k] * T[k + 1][j] +
                                F[i][k] * F[k + 1][j])
            i += 1
    return T[0][n - 1]
 
 
# Driver Code
symbols = "TTFT"
operators = "|&^"
n = len(symbols)
 
# There are 4 ways
# ((T|T)&(F^T)), (T|(T&(F^T))),
# (((T|T)&F)^T) and (T|((T&F)^T))
print(countParenth(symbols, operators, n))

# Time Complexity: O(n3) Auxiliary Space: O(n2)



""" Approach 2: 
We can also use recursive approach (Top Down dp), this approach uses memoization."""

def parenthesis_count(Str, i, j, isTrue, dp) :
    if (i > j) : return 0
     
    if (i == j) :
        if (isTrue == 1): return 1 if Str[i] == 'T' else 0
        else: return 1 if Str[i] == 'F' else 0
     
    if (dp[i][j][isTrue] != -1): return dp[i][j][isTrue]
     
    temp_ans = 0
    
    for k in range(i + 1, j, 2) :
     
        if (dp[i][k - 1][1] != -1) :
            leftTrue = dp[i][k - 1][1]
        else :
            # Count number of True in left Partition
            leftTrue = parenthesis_count(Str, i, k - 1, 1, dp)
         
        if (dp[i][k - 1][0] != -1) :
            leftFalse = dp[i][k - 1][0]
        else :
        # Count number of False in left Partition
            leftFalse = parenthesis_count(Str, i, k - 1, 0, dp)
      
        if (dp[k + 1][j][1] != -1) :
            rightTrue = dp[k + 1][j][1]
        else :
        # Count number of True in right Partition
            rightTrue = parenthesis_count(Str, k + 1, j, 1, dp)
       
        if (dp[k + 1][j][0] != -1) :
            rightFalse = dp[k + 1][j][0]
        else :
        # Count number of False in right Partition
            rightFalse = parenthesis_count(Str, k + 1, j, 0, dp)
     
      # Evaluate AND operation
        if (Str[k] == '&') :
            if (isTrue == 1) :
                temp_ans = temp_ans + leftTrue * rightTrue
            else :
                temp_ans = temp_ans + leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse
      # Evaluate OR operation
        elif (Str[k] == '|') :
            if (isTrue == 1) :
                temp_ans = temp_ans + leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
            else :
                temp_ans = temp_ans + leftFalse * rightFalse
     
      # Evaluate XOR operation
        elif (Str[k] == '^') :
            if (isTrue == 1) :
                temp_ans = temp_ans + leftTrue * rightFalse + leftFalse * rightTrue
            else :
                temp_ans = temp_ans + leftTrue * rightTrue + leftFalse * rightFalse
        dp[i][j][isTrue] = temp_ans
 
    return temp_ans
     
def countWays(N, S) :
  
    dp = [[[-1 for k in range(2)] for i in range(N + 1)] for j in range(N + 1)]
    return parenthesis_count(S, 0, N - 1, 1, dp)
  

symbols = "TTFT"
operators = "|&^"
S = ""
j = 0
for i in range(len(symbols)) :
 
  S = S + symbols[i]
  if (j < len(operators)) :
    S = S + operators[j]
    j += 1
 
# We obtain the string  T|T&F^T
N = len(S)
 
# There are 4 ways
# ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and
# (T|((T&F)^T))
print(countWays(N, S))
