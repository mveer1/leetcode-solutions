from math import *

def fun1(n):
    # T.C = O(n)
    div1 = []
    for i in range(1,n+1): # [1,n]
        if n%i == 0:
            div1.append(i)
    return div1

def fun2(n):
    # T.C = O(root(n))
    div2 = set()
    for i in range(1,int(sqrt(n))+1): # [1,root(n)]
        if n%i == 0:
            div2.add(i)
            div2.add(n//i)
    return list(div2)
