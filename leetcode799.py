
# auther yeling
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7


class Solution:
    def champagneTower2(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_row + 1) for _ in range(query_row + 1)]
        dp[0][0] = poured
        for i in range(1, query_row + 1):
            for j in range(i+1):
                if dp[i - 1][j] > 1:
                    dp[i][j] = (dp[i - 1][j] - 1) / 2
                if j > 0 and dp[i-1][j-1] > 1:
                    dp[i][j] += (dp[i-1][j-1] - 1)/2

        return dp[query_row][query_glass]

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_row + 1) for _ in range(query_row + 1)]
        dp[0][0] = poured
        for i in range(1, query_row + 1):
            for j in range(i+1):
                if dp[i - 1][j] >= 1:
                    dp[i][j] = (dp[i - 1][j] - 1) / 2
                if j > 0 and dp[i-1][j-1] > 1:
                    dp[i][j] += (dp[i-1][j-1] - 1)/2
        res = dp[query_row][query_glass]
        if res > 1.0:
            res = 1.0
        return res


poured = 2
query_row = 1
query_glass = 1
poured = 100000009
query_row = 33
query_glass = 17

sol = Solution()
print(sol.champagneTower(poured, query_row, query_glass))
