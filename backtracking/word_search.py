# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#   A   B   C   E
#   S   F   C   F
#   A   D   E   E

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass