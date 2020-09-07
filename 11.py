'''
11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        max=maxHeight= 0
        if len(height)<2: return max
        for i in range(0, len(height)-1):
            if height[i]<maxHeight: continue
            maxHeight=height[i]
            maxInnerH = 0
            for j in range(len(height)-1, i, -1):
                if height[j]<maxInnerH: continue
                maxInnerH = height[j]
                h = height[i] if height[i]<height[j] else height[j]
                v = h*(j-i)
                max = v if max<v else max
        return max
        '''
        '''
        left, right = 0, len(height) - 1
        ans = min(height[left], height[right]) * right
        while left < right:
            if height[left] <= height[right]:
                left += 1
                while left < right and height[left] <= height[right]:
                    area = height[left] * (right - left)
                    ans = area if area > ans else ans
                    left += 1
                if left < right:
                    area = height[right] * (right - left)
                    ans = area if area > ans else ans
                else: return ans
            else:
                right -= 1
                while left < right and height[right] < height[left]:
                    area = height[right] * (right - left)
                    ans = area if area > ans else ans
                    right -= 1
                if left < right:
                    area = height[left] * (right - left)
                    ans = area if area > ans else ans
                else: return ans
        return ans
        '''
        '''
        we use double pointers to traverse the list. 
        Complexity: time O(n); space O(1)
        '''
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            ans = max(ans, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        return ans