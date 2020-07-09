'''
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]


'''

class Solution:
    '''
    The basic idea for this solution is to use a set to speed up the lookup process. 
    The trick is how we deal with duplicates. 
    First we sort this list so that duplicates are grouped together, also we can make sure
    the qualified triples (a list) are in ascending order to eliminate duplicates in the 
    answer. 
    Then we use a double loop to check for every pair in the list, if the qualified third 
    number is also in the list. To avoid duplicates in the answer, for each loop, if the 
    current element is the same as previous one, we skip it. The lookup of the third num
    can be done in O(1) by using the set of unique elements.Some tricks:
    1. if the sum of the first two nums are greater than 0, since the list is sorted, we       can stop the second loop and continue with the next number in the first loop.
    2. we need to make sure the third num is no smaller than the second one
    3. if the third num == the second num, we need to make sure the second num is not 
    unique in nums, i.e. it has duplicates
    
    Complexity: time O(n * n); space O(n)
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        length = len(nums)
        if length < 3: return r
        nums.sort()
        uniqueNums = {num for num in nums}
        i, end, end1= 0, length - 2, length - 1
        while i < end:
            while i > 0 and i < end and nums[i] == nums[i - 1]: i += 1
            j = i + 1
            while j < end1:
                while j > i + 1 and j < end1 and nums[j] == nums[j - 1]: j += 1
                if j == end1: break
                total2 = nums[i] + nums[j]
                third = 0 - total2
                if total2 > 0 or third < nums[j]: break
                if third in uniqueNums:
                    if third == nums[j] and nums[j] != nums[j+1]: pass
                    else: r.append([nums[i], nums[j], third])
                j += 1
            i += 1
        return r