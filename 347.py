'''
347. Top K Frequent Elements
Medium

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    You can return the answer in any order.
'''

from collections import Counter
class Solution:
    '''
    We can first construct a dictionary (num->frequency), sort the keys based on values
    then return the first k elements
    Complexity: time O(nlogn) space O(n)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic: dic[num] += 1
            else: dic[num] = 1
        return sorted(dic, key=lambda x:-dic[x])[0:k]
        '''
        # use collections.Counter 
        return list(map(lambda x: x[0], Counter(nums).most_common(k)))
    '''
'''
# bucket sort method
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: bucket[freq].append(num) 
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]
'''