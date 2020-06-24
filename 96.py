'''
LeetCode 96
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


'''

'''

'''

class Solution:
    
    '''
    My solution: O(n*n) Space(n)
    Use the idea of dynamic programming. Say n = 5, we have 5 types of BSTs with 1-5 as root. 
    For any type, say 3 as the root, the number of BSTs is determined by (#_left_nodes * #_right_nodes)
    Thus, f(n) = f(0)*f(n-1) + ... + f(n-1)*f(0)
    Also, note that f(0)*f(n-1) == f(n-1)*f(0)
    
    def numTrees(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        nums = [1, 1]
        for num in range(2, n+1):
            val = 0
            left, right = 0, num - 1
            while left < right:
                val += 2 * nums[left] * nums[right]
                left += 1
                right -= 1
            if left == right: val += nums[left]**2
            nums.append(val)
        return nums[n]
     '''
    
    '''
    A better solution. 
    Catalan Numbers Formula: 
    f[n] = f[0]*f[n-1] + f[1]*f[n-2] + ... + f[n-2]*f[1] + f[n-1]*f[0] = (2n)!/(n! * n! * (n+1)).
    '''
    def numTrees(self, n):
        return factorial(2*n)//factorial(n)//factorial(n)//(n+1)