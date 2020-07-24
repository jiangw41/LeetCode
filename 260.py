'''
260. Single Number III
Medium

Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

Note:

    The order of the result is not important. So in the above example, [5, 3] is also correct.
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
'''
class Solution:
    '''
    This question is a little harder than the original single number problem where there is only one single number. However, we can use the same strategy to solve it. First we ^ all numbers in nums, and apparently the result is the ^ of those two unique numbers. All the set bits of the result are where those two numbers are different. We keep shift the result to the right to find the first set bit from the right. Based on whether this bit is 0 or 1, we can divide nums into two groups and ^ each group to get each number. 
    Complexity: time O(n), space O(1)
    '''
    def singleNumber(self, nums: List[int]) -> List[int]:
        t = 0
        for num in nums: t ^= num
        times = 0
        while not (t & 1): 
            t >>= 1
            times += 1
        t = 1 << times
        
        a = b = 0
        for num in nums:
            if num & t: a ^= num
            else: b ^= num
        return [a, b]