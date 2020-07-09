'''
LC 662. Maximum Width of Binary Tree
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    For this problem, we run BFS on each level, save the all the nodes in a list
    and check its width on this level, i.e. the distance between the leftmost and 
    rightmost non-null nodes. Then go to the next level. 
    
    The trick is when saving the nodes, we also need to save its relative order
    as shown below:
           0
          / \
         0   1
        / \ / \
       0  1 2  3
    
    complexity: time O(m * n); space O(n) where m, n is the depth and max number nodes
    on each level. 
    '''
    def widthOfBinaryTree(self, root: TreeNode) -> int:     
        if not root: return 0
        r = 1
        stack = [(root, 0)]
        while stack:
            length = len(stack)
            if length == 1: candidate = 1
            else: candidate = stack[-1][1] - stack[0][1] + 1
            r = max(r, candidate)
            for _ in range(length):
                node, order = stack.pop(0)
                if node.left: stack.append((node.left, 2 * order))
                if node.right: stack.append((node.right, 2 * order + 1))
        return r
        
        
        
        