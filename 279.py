'''
LC 279 Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
class Solution:
	'''
    we use dynamic programming. Starting from 0, we store the least number of perfect
    numbers for each number until n. We have a list to store the perfect numbers that 
    are smaller than the current number. For the current number, if it equals to the 
    next perfect number, then the least numer is 1. Otherwise we will try to deduct 
    all possible perfect square numbers one at a time to find the least number. 

    Complexsity: time O(n^2); space O(n)
	'''

    def numSquares(self, n: int) -> int:
        squares, visited = [], [0]
        next = 1
        nextSquare = 1
        num = 1
        while num <= n:
            if num == nextSquare:
                visited.append(1)
                squares.insert(0, num)
                next += 1
                nextSquare = next * next
            else:
                minNum = 1 + visited[num - squares[0]]
                for square in squares[1:]:
                    candidate = 1 + visited[num - square]
                    if candidate < minNum:
                        minNum = candidate
                visited.append(minNum)
            num += 1
        return visited[n]
            