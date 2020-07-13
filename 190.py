'''
190. Reverse Bits
Easy

Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
'''
class Solution:
    '''
    The problem has various solutions, such as bit to bit operations, divide and 
    conque, pure mathematical and bit operations (see solutions). Here we use
    builtin function bin() to convert n to its binary form (a string) and           calculate the number of left padding 0s. Then we reverse this string,
    convert it to a number and add the number of 0s on the left to its right to
    get the result. 
    
    Complexity: time, space O(1)
    '''
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:][::-1]
        left = 32 - len(binary)
        ans = 0
        for bit in binary:
            if bit == '0': ans <<= 1
            else: 
                ans = (ans << 1) | 1
        ans <<= left
        return ans