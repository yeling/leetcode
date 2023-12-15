
# auther yeling
# 1947. 最大兼容性评分和
from typing import List
from bisect import *


class Solution:
    # 全排列
    def maxCompatibilitySum2(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        n = len(students[0])
        val = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                sum = 0
                for k in range(n):
                    if students[i][k] == mentors[j][k]:
                        sum += 1
                val[i][j] = sum
        # print(val)
        used = [False] * m
        global res
        res = 0
        def dfs(index, used, preLen, preSum):
            if preLen == m:
                global res
                res = max(res, preSum)
                # print('dfs', index, used, preSum)
            for i in range(m):
                if used[i] == False:
                    used[i] = True
                    dfs(i, used, preLen + 1, preSum + val[preLen][i])
                    used[i] = False
                    # use
            return

        dfs(0, used, 0, 0)
        return res
    
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        n = len(students[0])
        val = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                sum = 0
                for k in range(n):
                    if students[i][k] == mentors[j][k]:
                        sum += 1
                val[i][j] = sum
        dpLen = 1 << m
        dp = [0] * dpLen
        for i in range(dpLen):
            count = bin(i).count('1')
            for j in range(m):
                if (i >> j) & 1:
                    dp[i] = max(dp[i], dp[i^(1<<j)] + val[count - 1][j])
            
        return dp[dpLen - 1]
    


students = [[1, 1, 0], [1, 0, 1], [0, 0, 1]]
mentors = [[1, 0, 0], [0, 0, 1], [1, 1, 0]]

# students = [[0,0],[0,0],[0,0]]
# mentors = [[1,1],[1,1],[1,1]]

sol = Solution()
print(sol.maxCompatibilitySum(students, mentors))
