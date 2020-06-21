'''
LeetCode 174

'''

class Solution:
    '''
    runtime: 87% memory: 25%
    using dynamic programming
    starting from bottom right cell, each cell is changed to a value which denotes 
    the minimum health value to enter this cell, determined by the original value 
    in the cell and the minimum health values in the cell below and the cell on the 
    right (if not on the border)
    '''
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # edge case 1: no cell
        if not dungeon or not dungeon[0]: return 1
        width, length = len(dungeon)-1, len(dungeon[0])-1
       
        # edge case 2: only one cell
        if width == length == 0:
            return 1 if dungeon[0][0] >= 0 else (1-dungeon[0][0])
        
        # multiple cells, starting from the bottom right corner
        i, j = width, length
        while i >= 0 and j >= 0:
            # first change the value of bottom right corner
            if i == width and j == length:
                dungeon[i][j] = 1 if dungeon[i][j] >= 0 else (1 - dungeon[i][j])
            else:
                val = min(dungeon[i+1][j], dungeon[i][j+1])
                if dungeon[i][j] >= val: dungeon[i][j] = 1
                else: dungeon[i][j] = val - dungeon[i][j]
            
            # we have reached the first cell
            if i == j == 0:
                return dungeon[0][0]
            
            # on the top border
            elif i == 0:
                j -= 1
                while j >= 0:
                    if width > 0: val = min(dungeon[1][j], dungeon[0][j+1])
                    else: val = dungeon[0][j+1]
                    dungeon[0][j] = 1 if dungeon[0][j] >= val else (val - dungeon[0][j])
                    j -= 1
                return dungeon[0][0]    
            
            # on the left border
            elif j == 0:            
                i -= 1
                while i >= 0:
                    if length > 0: val = min(dungeon[i][1], dungeon[i+1][0])
                    else: val = dungeon[i+1][0]  
                    dungeon[i][0] = 1 if dungeon[i][0] >= val else (val - dungeon[i][0])
                    i -= 1
                return dungeon[0][0]                 
                
            else: 
                # change cells on the same row
                c = j - 1
                while c >= 0:
                    if i == width: val = dungeon[i][c+1]
                    else: val = min(dungeon[i][c+1], dungeon[i+1][c])
                    dungeon[i][c] = 1 if dungeon[i][c] >= val else (val - dungeon[i][c])
                    c -= 1 
                
                # change cells on the same column
                c = i - 1
                while c >= 0:
                    if j == length: val = dungeon[c+1][j]
                    else: val = min(dungeon[c+1][j], dungeon[c][j+1])
                    dungeon[c][j] = 1 if dungeon[c][j] >= val else (val - dungeon[c][j])
                    c -= 1
  
            i -= 1
            j -= 1
                
                
        