
# auther yeling
from typing import List
import math


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
        # 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
        # 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
        # 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
        dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[0,-1],[1,-1],[1,0],[1,1]]
        nb = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                nb[i][j] = board[i][j]

        for i in range(len(board)):
            for j in range(len(board[i])):
                sum = 0
                for de in dirs:
                    next = [de[0] + i, de[1] + j]
                    if next[0] >= 0 and next[0] < len(board) and next[1] >= 0 and next[1] < len(board[i]):
                        if nb[next[0]][next[1]] == 1:
                            sum += 1
                
                if nb[i][j] == 1 and (sum < 2 or sum > 3):
                    board[i][j] = 0
                elif nb[i][j] == 0 and sum == 3:
                    board[i][j] = 1
        


sol = Solution()
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
sol.gameOfLife(board)
print(board)
