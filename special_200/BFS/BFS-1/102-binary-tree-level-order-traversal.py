
"""
102. Binary Tree Level Order Traversal
Medium
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 
Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000


"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Accepted
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Explanation: Level order traversal is essentially BFS. 
        But in order to get the levels, we need to keep track of the size of the queue. AKA SIZE VARIABLE.
        We update the size variable at the end of each level. Beginning at the head its 1, then 2, then 4, then 8, etc.
        once a level is processed, the remaining nodes in the queue are the nodes in the next level. 
        SO, we update the size variable to the length of the queue.
        
        Generate a list for each level and append it to the result list.
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        lis = []
        q = deque()
        q.append(root)
        while len(q) > 0:
            size = len(q) # size of the current level
            level = []
            for i in range(size): # going over one level at a time
                curr = q.popleft()
                level.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            lis.append(level)
        return lis

LeetCode(PROBLEM, Solution).check()
