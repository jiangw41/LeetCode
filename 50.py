'''
50. Pow(x, n)
Medium

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:

    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]

'''

class Solution:
    '''
    First, we need to check whether n is less than, equal or greater than 0. When n is a positive int, say 7, to calculate pow(x, n), instead multiply x by x 7 times, we can do this x * (x^2) * (x^4), note that x * x = (x^2) and (x^2) * (x^2) = (x^4). This corresponds to its binary form (7 = 111). So we can keep shift n to the right 1 by 1 until it reaches 0 and every time x becomes x * x. 
    Complexity: time O(logn) space(1)
    '''
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        isNeg = False
        if n < 0: 
            isNeg = True
            n = -n
        r = 1
        val = x
        while n:
            if n & 1: r *= val
            n >>= 1
            val *= val
        if isNeg: return 1/r
        return r
        
        