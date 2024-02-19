
"""
1035. Cousins in Binary Tree
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
Two nodes of a binary tree are cousins if they have the same depth with different parents.
Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
 
Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

 
Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.


"""
from collections import deque 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Accepted
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Explanation: BFS with a queue and a parent queue.
    The intuition is that while going throuhg the nodes in each level, we keep track of the parent node.
    we use a parallel queue to keep track of the parent node.
    
    ALgorithm: Nodes should be cousins if they are in the same level and have different parents.
        check this condition while traversing the tree and maintain the parent nodes if the current node is x or y.
        check and return the result.
    
    """
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None: return []
        q = deque()
        pq = deque()
        pq.append(None)
        q.append(root)
        x_parent = None
        y_parent = None
        while len(q) > 0:
            size = len(q) # size variable for level maintainance
            for i in range(size): # process each level
                curr = q.popleft()
                curr_parent = pq.popleft()
                if curr.val == x:
                    x_parent = curr_parent
                elif curr.val == y:
                    y_parent = curr_parent
                if curr.left: 
                    q.append(curr.left)
                    pq.append(curr)
                if curr.right: 
                    q.append(curr.right)
                    pq.append(curr)
            # these two conditions are for the case only one of the nodes is found in a level
            # so obviously, they are not cousins because they are not in the same level
            if x_parent and not y_parent:
                return False
            if y_parent and not x_parent:
                return False
        if x_parent == y_parent: # if found on same level, check if they have the same parent
            return False
        return True

LeetCode(PROBLEM, Solution).check()
