'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199

Constraints:

    num consists only of digits '0'-'9'.
    1 <= num.length <= 35

Follow up:
How would you handle overflow for very large input integers?
'''

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # time (n^2), beats 80%; space(1), beats 77.83%
        # the key is to find what the first two numbers are
        # brute force check
        length = len(num)
        # the first two numbers takes at most 2/3 total digits
        # that is how many digits we need to check
        allowed = length * 2 // 3
        
        # a number takes at least one digit
        for firstdigits in range(1, allowed):
            # a number of 2 or more digits cannot start with 0
            if num[0] == '0' and firstdigits > 1: break
                
            for seconddigits in range(1, allowed + 1 - firstdigits):
                # a number of 2 or more digits cannot start with 0
                if num[firstdigits] == '0' and seconddigits > 1: break
                totaldigits = firstdigits + seconddigits
                second = int(num[firstdigits:totaldigits])
                total = str(int(num[:firstdigits]) + second)
                # total is found at the head
                if num[totaldigits:].find(total) == 0:
                    s = num[totaldigits+len(total):]
                    first = second
                    second = int(total)
                    
                    # continue to check the following digits
                    while s:
                        total = first + second
                        if s.find(str(total)) == 0:
                            first = second
                            second = total
                            s = s[len(str(total)):]
                        else: break
                        
                    if not s: return True
        return False