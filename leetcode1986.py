
# auther yeling
from typing import List
import math


class Solution:
    # 87 / 96 贪心
    def minSessions2(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort(reverse=True)
        sum = 0
        while True:
            print(tasks)
            curr = sessionTime
            find = False
            for i, v in enumerate(tasks):
                if v != 0 and v <= curr:
                    curr = curr - tasks[i]
                    tasks[i] = 0
                    find = True
            tasks.sort(reverse=True)
            if find == False:
                break
            sum += 1
        return sum

    #背包问题，动态规划
    #状态DP
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        m = 1 << n
        dp = [n]*m
        
        #每个状态的初始值
        for i in range(0,m):
            spend = 0
            id = 0
            state = i
            while state > 0:
                if state & 1 == 1:
                    spend += tasks[id]
                state >>= 1
                id += 1
            if spend <= sessionTime:
                dp[i] = 1

        # print(dp)
        for i in range(m):            
            if dp[i] == 1:
                continue
            split = i >> 1
            #去除低位的1
            j = (i - 1) & i
            while j > split:
                # dp[j] 子集 dp[i^j] 补集
                dp[i] = min(dp[i], dp[j] + dp[i^j])
                j = (j - 1) & i
            # print(dp)

        return dp[m - 1]


sol = Solution()

# tasks = [1, 2, 3]
# sessionTime = 3

tasks = [3, 1, 3, 1, 1]
sessionTime = 8

# tasks = [1, 2, 3, 4, 5]
# sessionTime = 15

# tasks = [2,3,3,4,4,4,5,6,7,10]
# sessionTime = 12

print(sol.minSessions(tasks, sessionTime))
