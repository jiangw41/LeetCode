'''
LC 957. Prison Cells After N Days
Medium

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

    If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
    Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

 

Example 1:

Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:

Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]

 

Note:

    cells.length == 8
    cells[i] is in {0, 1}
    1 <= N <= 10^9

'''

class Solution:
    '''
    The key to this problem is that a loop can form after enough days. 
    First we get the first day's state and save it. Then we proceed day by day. 
    There are two cases: a loop detected before we finish or no loop detected. 
    Complexity: time O(K) where K is the number of days in a loop; space O(1)
    '''
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        # day 1
        index = 1
        previous = cells[0]
        while index < 7:   
            t = 1 ^ previous ^ cells[index+1]    
            previous = cells[index]
            cells[index] = t
            index += 1
        # after day 1, those two cells are always empty
        cells[0] = cells[7] = 0
        # save day 1's state for future loop detection
        tem = cells.copy()
        N -= 1
        
        # used to count where the loop starts
        counter = 0
        for _ in range(N):
            counter += 1
            N -= 1
            index = 1
            previous = 0
            while index < 7:
                t = 1 ^ previous ^ cells[index+1]
                previous = cells[index]
                cells[index] = t
                index += 1
            # loop detected
            if cells == tem: break
        # finish before loop forms 
        if not N: return cells  
        
        N %= counter
        for _ in range(N):
            index = 1
            previous = 0
            while index < 7:
                t = 1 ^ previous ^ cells[index+1]
                previous = cells[index]
                cells[index] = t
                index += 1
        return cells