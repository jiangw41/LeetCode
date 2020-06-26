'''
LC 1
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
We are trading space for time by using a dictionary. 
time O(n); space O(n)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            if (target - num) in dic:
                return [index, dic[target - num]]
            else: dic[num] = index
