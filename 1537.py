'''
1537. Get the Maximum Score
Hard

You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:

    Choose array nums1 or nums2 to traverse (from index-0).
    Traverse the current array from left to right.
    If you are reading any value that is present in nums1 and nums2 you are allowed to change your path to the other array. (Only one repeated value is considered in the valid path).

Score is defined as the sum of uniques values in a valid path.

Return the maximum score you can obtain of all possible valid paths.

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
Output: 30
Explanation: Valid paths:
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],  (starting from nums1)
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]    (starting from nums2)
The maximum is obtained with the path in green [2,4,6,8,10].

Example 2:

Input: nums1 = [1,3,5,7,9], nums2 = [3,5,100]
Output: 109
Explanation: Maximum sum is obtained with the path [1,3,5,100].

Example 3:

Input: nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
Output: 40
Explanation: There are no common elements between nums1 and nums2.
Maximum sum is obtained with the path [6,7,8,9,10].

Example 4:

Input: nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
Output: 61

 

Constraints:

    1 <= nums1.length <= 10^5
    1 <= nums2.length <= 10^5
    1 <= nums1[i], nums2[i] <= 10^7
    nums1 and nums2 are strictly increasing.
'''
'''
First we define parallel subarrays of two arrays are a pair of subarrays (note they belong to different arrays) where: 
1. Their heads are the heads of their parent arrays or their heads are equal, and 
2. Their ends are the ends of their parent arrays or their ends are equal. 

The problem can be solved by finding all the pairs of parallel subarrays and adding the bigger of the two sums of each subarray. 

Complexity: time O(m+n); space O(1) where m, n are lengths of nums1, nums2
'''
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        c1 = c2 = 0
        len1, len2 = len(nums1), len(nums2)
        ans = 0
        t1 = t2 = 0
        while c1 < len1 and c2 < len2:
            if nums1[c1] < nums2[c2]: 
                t1 += nums1[c1]
                c1 += 1
            elif nums1[c1] > nums2[c2]: 
                t2 += nums2[c2]
                c2 += 1
            else: 
                ans += max(t1, t2) + nums1[c1]
                t1 = t2 = 0
                c1 += 1
                c2 += 1
        return (ans + max(t1 + sum(nums1[c1:]), t2 + sum(nums2[c2:]))) % (10**9 + 7)
