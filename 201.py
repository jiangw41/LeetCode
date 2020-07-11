'''
201. Bitwise AND of Numbers Range
Medium

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4

Example 2:

Input: [0,1]
Output: 0
'''
class Solution:
    '''
    The key to this problem is to find the common prefix.
    We can continuously shift m and n to the right until m becomes 0 or m == n. 
    Then we shift m to the left the number of bits we shift in the previous step. 
    
    Complexity: time O(logm); space O(1)
    '''
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        c = 0
        while m and m != n:
            m >>= 1
            n >>= 1
            c += 1
        if not m: return 0
        return m << c