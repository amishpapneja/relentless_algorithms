
"""
542. 01 Matrix
Medium
TODO: Try with DFS also
"""
from collections import deque
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
 
Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

 
Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.


"""

class Solution:
    """
    Accepted
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    
    Approach [Collective BFS on all 0s]:
    - intuition is to start from all the zeros and find ones while maintaining the level. TO make it easy, we mark all the 1s as -1
    - Add all 0s to the queue and start BFS
    - Start BFS from all 0s and add all the neighbors to the queue
    - Poll and whenever -1 is found, update the answer level that is the distance from the nearest 0
    - Continue until the queue is empty
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dirs = [
            [0,-1],
            [-1,0],
            [1,0],
            [0,1]
        ]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    mat[i][j] = -1 # mark all 1s as -1
                else:
                    q.append((i,j)) # add all 0s to the queue
        level = 0
        while len(q) > 0:
            flag = False
            size = len(q)
            if flag is True: break
            for i in range(size):
                curr = q.popleft()
                currValue = mat[curr[0]][curr[1]]
                if currValue == -1: # if -1 is found, update the answer level
                    mat[curr[0]][curr[1]] = level
                
                for dir in dirs: # add all the neighbors to the queue || Basic BFS
                    nr = dir[0] + curr[0]
                    nc = dir[1] + curr[1]
                    if 0 <= nr < m  and 0 <= nc < n and mat[nr][nc] < 0:
                        q.append((nr, nc))
            level += 1
        
        return mat
    """
    Not Accepted -TLE
    Time Complexity: O((m * n)^2). The time complexity is O(m*n) for each BFS traversal and we do this for m*n cells.
    Space Complexity: O(m*n) For the queue and visited set
    
    Approach: [One by One BFS]
    - intuition is to start from all the ones individually and find zeros while maintaining the level
    - For each one, start a fresh DFS, and find the nearest zero. If found, update the answer to level
    
    """
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dirs = [
            [0,-1],
            [-1,0],
            [1,0],
            [0,1]
        ]
        ones = []
        zeros = []
        for i in range(m):
            for j in range(n): # find all 1s and 0s
                if mat[i][j] == 1:
                    ones.append([i,j])
                    mat[i][j] = 1
                else:
                    zeros.append([i,j])

        for one in ones: # for each one, start a fresh DFS
            i, j = one[0], one[1]
            q = deque()
            q.append((i,j))
            level = 0
            flag = False
            visited = set()
            while len(q) > 0:
                size = len(q)
                if flag is True: break # if zero is found, break
                for _ in range(size):
                    curr = q.popleft()
                    visited.add(curr)
                    currValue = mat[curr[0]][curr[1]]
                    if currValue == 0: # at any point, if zero is found, update the answer to the current level
                        mat[i][j] = level
                        flag = True
                        break
                    for dir in dirs: # add all the neighbors to the queue || Basic BFS
                        nr = dir[0] + curr[0]
                        nc = dir[1] + curr[1]
                        if 0 <= nr < m  and 0 <= nc < n and (nr,nc) not in visited: # out of bounds or already visited check
                            q.append((nr, nc))
                level += 1
        return mat
    

LeetCode(PROBLEM, Solution).check()
