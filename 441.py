'''
441. Arranging Coins

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        we can use binary search 
        complexity: time O(lgn); spaceO(1)
        
        # the following edge case is covered by binary search
        #if n == 0: return 0
        left, right = 0, n
        t = 2 * n
        while left <= right:
            mid = (left+right) // 2
            val = mid * mid + mid
            if val == t:
                return mid
            elif val > t:
                right = mid - 1
            else: left = mid + 1
        return right
        '''
        # the best way is to use math calculation based on the fact that
        # r * (r+1) / 2 <= n
        # complexity: time O(1); space O(1)
        import math 
        return int(math.sqrt(2*n+0.25)-0.5)