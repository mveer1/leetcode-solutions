"""118. Pascal's Triangle
Given an integer numRows, return the first numRows of Pascal's triangle.

mysol:
"""
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        tri = list()
        tri.append([1])
        rownum = 2
        
        while rownum<=numRows:
            subtri = [1]
            for i in range(1, rownum-1):
                subtri.append(tri[-1][i-1]+tri[-1][i])
            subtri.append(1)
            tri.append(subtri)
            rownum +=1
        return tri

#could be faster when assignment is used instead of append.

class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle

#both solutions, O(n^2) for time and space.












"""119. Pascal's Triangle II
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

mysol:
"""
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        #direct approch would be and return the last row.
        
        #this approch does it in O(n) time
        prev = 1
        ans = [None]*(rowIndex+1)
        ans[0] = 1
        for i in range(1,rowIndex+1):            
            curr = (prev * (rowIndex - i + 1)) // i
            ans[i] = curr
            prev = curr
        return ans

#could also be done more simply with append, this is faster ig
