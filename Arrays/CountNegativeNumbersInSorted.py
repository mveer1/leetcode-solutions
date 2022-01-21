"""1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

mysol 98%:
"""
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m = len(grid)-1
        n = len(grid[0])-1
        j = n
        i = 0
        c = 0
        while i<=m and j>=0:
            if grid[i][j]<0:
                # print("found at", i,j, "adding", m-i+1)
                j -= 1
                c += m-i+1
            else:
                i +=1
        return c

"""
We can optimize more by using binary search to search the first the index in every row.
Time: O(nlogm)
Python solution:
"""
class Solution:
    def firstIndex(self, arr):
        start = 0
        end = len(arr) -1
        count = 0
        location = -1
        while start <= end:
            mid = start + (end - start)//2
            if (arr[mid] < 0):
                location = mid
                end = mid - 1;
            else:
                start = mid + 1
        return location
    def countNegatives(self, grid: list[list[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        i = 0
        j = 0
        count = 0
        while i < row:
            first = self.firstIndex(grid[i])
            if first >= 0:
                count += (col - first)
                i += 1
            else:
                i += 1
        return count


# another using binary search:
class Solution(object):
    def countNegatives(self, grid: list[list[int]]) -> int:
        def find_negative(row):
            left, right = 0, len(row)
            while left<right:
                mid = left + (right-left) // 2
                if row[mid]<0:
                    right = mid
                else:
                    left = mid+1
            return len(row)- left
        
        count = 0
        for i in grid:
            count += find_negative(i)
        return(count)
