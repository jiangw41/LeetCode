'''
LC 461. Hamming Distance
Easy

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.

'''

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # first we can do x ^ y then count the number of 1s in the result
        #return bin(x ^ y).count("1")
        x ^= y
        counter = 0
        while x:
            
            # counter += x % 2
            counter += x & 1
            
            # x //= 2
            x >>= 1
        return int(counter)