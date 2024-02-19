
"""
199. Binary Tree Right Side View
Medium
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
 
Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []

 
Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


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
    
    Explanation: The right side view is essesntially the last node in each level.
    Do the normal BFS, and at the end of each level, capture the last node.
    That's it.
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: return []
        lis = []
        q = deque()
        q.append(root)
        while len(q) > 0: # normal BFS
            size = len(q)
            curr = None
            for i in range(size):
                curr = q.popleft()
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            lis.append(curr.val) #level complete, save the last node
        return lis

LeetCode(PROBLEM, Solution).check()
