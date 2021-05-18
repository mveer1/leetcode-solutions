# A = LIST
# KEY = TARGET VALUE
# SORTED ARRAY
# TIME COMP = O(LOGN) 
# SPACE COMP = O(LOGN) (RECURSIVE) 
# SPACE COMP = O(1) (ITERATIVE)
def binSearch(A,left,right,key):
    while left <= right:
        mid = (left+right) // 2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            left = mid+1
        else:
            # key < A[mid]
            right = mid -1
    return -1
A = [25,35,80,96,200,500,850,999]
KEY = 200
binSearch(A,0,len(A)-1,KEY)
            
# Bisect acts as a binary search
import bisect
A = [25,35,80,96,200,500,850,999]
KEY = 200
bisect.bisect_left(A,KEY,0,len(A))



# A = List
# K = Target
# Unsorted List
def findTargetPair(A,K):
    st = set()
    for i in range(len(A)):
        complement = K - A[i]
        if complement in st:
            return [complement,A[i]]
        else:
            st.add(A[i])
            
A = [5,100,50,10,30,5,7,85,90,100]
K = 17
findTargetPair(A,K)