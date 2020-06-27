'''
1493. Longest Subarray of 1's After Deleting One Element
Medium

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.

 
Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4

Example 5:

Input: nums = [0,0,0]
Output: 0

 

Constraints:

    1 <= nums.length <= 10^5
    nums[i] is either 0 or 1.
'''

class Solution:
    '''
    first we need to check some edge cases
    then we find all indexes of 0 in nums and store them in a list
    check some edge cases again
    go over the list of indexes for 0, try to remove one and see what we can get
    update the result if necessary
    '''
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        # only one number
        if length == 1: return 0

        # all indexes of 0
        zeros = []
        # it indicates whether there is 1 in nums
        has1 = False
        for index, num in enumerate(nums):
            if num == 1: has1 = True
            else: zeros.append(index)

        # there is no 1
        if not has1: return 0

        # there is no 0
        if not zeros: return length - 1


        length0 = len(zeros)
        # there is only one 1 
        if length - length0 == 1: return 1

        # there is only one 0
        if length0 == 1: return length - 1

        # there are multiple 1s and 0s

        # remove first 0
        r = zeros[1]-1

        # remove last 0
        t = length - 2 - zeros[-2] 
        r = t if t > r else r

        # remove 0 somewhere between first and last 0
        index = 1
        while index < length0 - 1:
            t = zeros[index+1]-2-zeros[index-1]
            r = t if t > r else r
            index += 1
        return r
