'''
LC 107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    we use bfs to visit every level and use a list (stack) to store nodes to be visited
    complexity: time O(v); space O(v) where v is the number of nodes
    '''
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        r = []
        if not root: return r
        stack = [root]
        while stack:
            length = len(stack)
            t = []
            for _ in range(length):
                node = stack.pop()
                t.insert(0, node.val)
                if node.right: stack.insert(0, node.right)
                if node.left: stack.insert(0, node.left)
            r.insert(0, t)
        return r
