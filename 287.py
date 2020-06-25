'''
LC 287
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

'''

class Solution:
    #Floyd's Tortoise and Hare (Cycle Detection) 
    # time O(n); space O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[0], nums[0]
        #Phase 1: fast moves twice as much as slow, stops when they meet
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow: break
        fast = nums[0]
        #Phase 2: fast starts at index 0 and moves in the same speed
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        #Finally, they meet at the cycle's starting point
        return fast

'''
my dictionary solution, but it violates the constant space constraint. 
We could also use set, but it also violates the constant space constraint. 
time and space: O(N) 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        val = True
        dic = dict.fromkeys(nums, val)
        for num in nums:
            if num not in dic: return num
            del dic[num]
'''      