'''
239. Sliding Window Maximum
Hard

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 

Constraints:

    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length

Accepted
292,512
Submissions
674,385
'''
class Solution:
	'''
	We use a double ended queue which is in descending order to keep track of the numbers in the current window. 
	Complexity: space O(k); time O(k*n) 
	'''
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans, lst = [], []
        for index in range(k):
            while lst and lst[-1] < nums[index]:
                lst.pop()
            lst.append(nums[index])
        ans.append(lst[0])
        index, end = k, len(nums) - 1
        while index <= end:
            if nums[index - k] == lst[0]:
                del lst[0]
            while lst and lst[-1] < nums[index]:
                lst.pop()
            lst.append(nums[index])
            ans.append(lst[0])
            index += 1
        return ans