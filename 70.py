'''
70. Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 

Constraints:

    1 <= n <= 45

'''

class Solution:
    '''
    We use dynamic programming method. When n >= 3, step(n) = step(n-1) + step(n-2). 
    Complexity: time O(n); space O(1)
    '''
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        pre2, pre1 = 1, 2
        for index in range(3, n):
            pre2, pre1 = pre1, pre1 + pre2
        return pre1 + pre2   