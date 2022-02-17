"""Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e., as 2 x 1 tile. 

Example:

Input: n = 4
Output: 5
Explanation:

For a 2 x 4 board, there are 3 ways
All 4 vertical (1 way)
All 4 horizontal (1 way)
2 vertical and 2 horizontal (3 ways)
"""

# same question as stair case ig

def tiles(n):
    if n == 0 or n == 1:
        return 1
    return tiles(n-1) + tiles(n-2)

print(tiles(4))
print(tiles(3))
