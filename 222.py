'''
222. Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        toVisit, r = [], 0
        if root: 
            cnode = root
            depth = 0
            level = 0
            while True:      
                while cnode.left and cnode.right:
                    level += 1
                    toVisit.append([cnode.left, level])
                    cnode = cnode.right
                    r += 1
                if cnode.left:
                    r += 2
                    depth = level + 1
                    break
                if not toVisit: return r+1
                if not depth: depth = level; r+=1
                else:
                    r += 1
                    if level > depth: depth = level; break
                    
                cnode, level = toVisit.pop()
            while toVisit:
                level = toVisit.pop()[1]
                for power in range(depth-level+1):
                    r += 2**power        
        return r
        