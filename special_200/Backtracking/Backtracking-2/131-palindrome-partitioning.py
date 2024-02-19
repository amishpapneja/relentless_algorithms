
"""
131. Palindrome Partitioning
Medium
"""
from leetcode_runner import LeetCode, TestCase, Args
from typing import *

PROBLEM = """
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
 
Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:
Input: s = "a"
Output: [["a"]]

 
Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.


"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pass

LeetCode(PROBLEM, Solution).check()
