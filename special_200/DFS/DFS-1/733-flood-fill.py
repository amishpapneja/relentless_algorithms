
"""
733. Flood Fill
Easy
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.
 
Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.

 
Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n


"""

class Solution:
    """
    Accepted
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    
    Approach:
    - DFS from the starting point
    - Change the color of the pixel if it is the old color, make sure to not chagne color if its not the old color
    - Continue DFS in all 4 directions
    - Base case: out of bounds or already colored
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [
            [0,1],
            [1,0],
            [0,-1],
            [-1,0]
        ]
        m = len(image)
        n = len(image[0])
        old = image[sr][sc]
        def dfs(i,j, image):
            if i < 0 or j < 0 or i>=m or j >=n or image[i][j] == color: # out of bounds or already colored
                return
            if image[i][j] == old: image[i][j] = color # if old color, change to new color || FILL
            else: return
            for dir in dirs: # color all 4 directions by DFS
                nr = i + dir[0]
                nc = j + dir[1]
                dfs(nr,nc,image)
        dfs(sr,sc,image)
        return image

LeetCode(PROBLEM, Solution).check()
