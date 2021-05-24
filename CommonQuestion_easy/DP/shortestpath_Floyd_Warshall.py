# Floyd Warshall All Pairs shortest path Algorithm
# single source shorted path is for one vertex
# all pairs shorted path is for V vertices

# time for Dijkstra Algorithm is O(Elog(v)) for 1 Vertex
# hence O(V*E*log(V)) for V vertices
# Min value of E is V-1 and Max is V^2       #aysmtotically

# Hence if we use Dijkstra Algorithm for V vertices, it runs at O(V^3LogV)
# But Floyd Warshalls runs at O(V^3)

INF = float('inf')
def printmatrix(m):
    r,c = len(m),len(m[0])
    for i in range(r):
        for j in range(c):
            print(m[i][j],end="\t")
        print()


v,e = map(int,input().split())
m = [[None]*v for i in range(v)]
for i in range(v):
    for j in range(v):
        if i == j:      # src = dst            
            m[i][j] = 0
        else:        # edge doesn't exist
            m[i][j] = INF

# take input values
for i in range(e):
    src,dst,wt = map(int,input().split())
    m[src][dst] = wt


printmatrix(m)
print("-------------------")

# apply our algo
# T.C = O(v^3)
for k in range(v):
    for i in range(v):
        for j in range(v):
            # cost of tmp path is less
            # update
            if m[i][k]+m[k][j] < m[i][j]:
                m[i][j] = m[i][k] + m[k][j]
printmatrix(m)




""" 
Test cases:
4 4
0 3 10
0 1 5
1 2 3
2 3 1
"""


"""3rd column shows the weight of the edge ofcourse"""