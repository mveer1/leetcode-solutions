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