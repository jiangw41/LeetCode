'''
463. Island Perimeter      Easy

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
 
Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
(see picture on Website)
'''

'''
The solution is pretty straightforward. We only need to know when to add edges. 
For any cell, if it is an island (1), its four edges may be or may not be counted into 
Perimeter. Take the left edge for example, it should be counted into perimeter when 
either it is on the edge of the grid or its left neighbour is not an island, i.e. 0
Complexity: time O(m * n) where m = grid.length and n = gird[0].length; space O(1)
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        r = 0
        height, length = len(grid), len(grid[0])
        for i in range(height):
            for j in range(length):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0: r += 1
                    if i == height - 1 or grid[i+1][j] == 0: r += 1
                    if j == 0 or grid[i][j-1] == 0: r += 1
                    if j == length - 1 or grid[i][j+1] == 0: r += 1
        return r
