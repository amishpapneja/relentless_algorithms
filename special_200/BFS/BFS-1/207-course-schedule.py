
"""
207. Course Schedule
Medium
"""
from collections import deque
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
 
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 
Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.


"""

class Solution:
    """
        Accepted
        Time Complexity: O(V+E) where V is the number of vertices and E is the number of edges. 
        Space Complexity: O(V+E)
        In this problem, it is O(numCourses + len(prerequisites))
        
        Explanation: We represented this as a connected graph, where each node is a course and each edge is a prerequisite.
        We maintain two data structures: freqs and deps. freqs is a list of the number of prerequisites for each course.
        And deps is essentially a dictionary such that the key is the course and the value is a list of the courses that depend on the key.
        We flipped the given prerequisites list to make it easier to traverse the graph.
        
        We then used a BFS to traverse the graph, starting from the nodes with no prerequisites. Becasue we can take that course first.
        We then decrement the number of prerequisites for each course that depends on the current course. 
        If the number of prerequisites is 0, then we can take that course next. We continue this process until we have no more courses to take. If we have no more courses to take,
        then we can finish all courses. Otherwise, we cannot finish all courses.
        
        
        For EX:
        prerequisites = [(1, 0), (2, 0), (3, 1), (3, 2)]
        numCourses = 4
         0
        / \
       1   2
        \ /
         3
         
        freqs will be  [0, 1, 1, 2] (representing the number of prerequisites for each course), 
        and deps will be {
            0: [1, 2], 
            1: [3], 
            2: [3], 
            3: []
            }
            
            The order that we take the courses will be 0, 1, 2, 3.

        """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        freqs = [0 for _ in range(numCourses)]
        deps = {_:[] for _ in range(numCourses)}
        for pre in prerequisites: # filling out freqs and deps
            if pre[1] in deps:
                deps[pre[1]].append(pre[0])
            freqs[pre[0]] += 1
        q = deque()
        for idx, i in enumerate(freqs): # starting from the courses with no prerequisites
            if i == 0:
                q.append(idx)
        while len(q) > 0: # BFS
            curr = q.popleft()
            print(curr)
            curr_deps = deps[curr]
            for dep in curr_deps: # go over the courses that depend on the current course
                freqs[dep] -= 1 # decrement the number of prerequisites becasue we have taken one of them
                if freqs[dep] == 0: q.append(dep) # if the number of prerequisites is 0, then we can take that course next || PUT IN QUEUE
        if sum(freqs) == 0:
            return True
        return False

LeetCode(PROBLEM, Solution).check()