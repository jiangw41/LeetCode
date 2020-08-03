'''
1536. Minimum Swaps to Arrange a Binary Grid
Medium

Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

Example 1:

Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3

Example 2:

Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.

Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 200
    grid[i][j] is 0 or 1
'''
'''
First, we count the number of consecutive 0's in the tail and save the results in a list(lst). The nature of the problem is to rearrange lst when necessary to make sure for 0 <= i < n, lst[i] + 1 <= n - i. 

Complexity: time O(n^2); space O(n) 
'''

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        def zeros(lst):
            c = 0
            for num in lst[-1::-1]:
                if not num: c += 1
                else: return c
            return c
        lst = []
        for nums in grid: lst.append(zeros(nums))
        ans, counter = 0, len(grid)-1
        lstIndex = 0
        print(lst)
        while counter:
            if lst[lstIndex] >= counter: 
                counter -= 1
                lstIndex += 1
            else: 
                c = lstIndex + 1
                ans += 1
                length = len(lst)
                while c < length:
                    if lst[c] >= counter: del lst[c]; break
                    c += 1
                    ans += 1
                if c == length: return -1
                counter -= 1
        return ans
                    

