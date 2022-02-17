# matrix:  
# moves right, upright, downright
# moves(x,y) = [(1,0), (1,1), (1,-1)]
#you can start anywhere in the first column, find max sum of numbers you can collect

moves = [(1,0), (1,1), (1,-1)]

def fmaxgold(mat):
    #iterate through rows
    for i in range(len(mat)):
        gold = 0 
        gold += mat[i][0]
        for j in range(1, len(mat[i])):
            #iterate through moves
            for move in moves:
                i2 = move[0] + i
                j2 = move[1] + j
                #check if i2,j2 is valid
                if 0<=i2<len(mat) and 0<=j2<len(mat[i]):
                    pass

def maxgold(i, j, mat):
    #first check if i,j is valid
    if not (0<=i<len(mat) and 0<=j<len(mat[i])):
        return 0
    # print("CHECKING FOR:", i, j, mat[i][j])
    return mat[i][j] + max(maxgold(i, j+1, mat), maxgold(i+1,j+1, mat), maxgold(i-1, j+1, mat))

mat = [[1, 3, 3],[2, 1, 4],[0, 6, 4]]


mat = [[10, 33, 13, 15],[22, 21, 4, 1], [5, 0, 2, 3], [0, 6, 14, 2]]

# gold = 0
# for i in range(len(mat)):
#     # print("row:", i)
#     gold = max(gold, (maxgold(i, 0, mat)))

# print(gold)