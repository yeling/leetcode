
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *
from math import *
from queue import PriorityQueue

INF = 2 ** 64 - 1
MOD = 10 ** 9 + 7

class Solution:
    #1.dp[i] i个box,所需要的搬运次数
    #2.dp[i] = min(dp[k] + f(k,i)) 前面k个中总重量不超过maxWeiht的搬运次数+后面搬运一次所需要的次数
    #3.dp[k] 单调递增，单调队列，每次栈顶存最小的，maxWeight从队列头部删除
    #dp[k - 1] > dp[k] dp[k]才是最佳选择, f(k - 1,i) >= f(k,i)
    # TLE 35 / 39
    # f(k,i) 遇到不同的码头加一，也可以表示为前缀和
    #两个前缀和 + 动态规划 + 单调队列
    def boxDelivering2(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        dp = [2 * (i + 1) for i in range(n)]
        pre = [0] * (n + 1)
        for i,v in enumerate(boxes):
            pre[i + 1] = pre[i] + v[1]

        def f(k,i):
            c = 1
            last = -1
            for j in range(i, k - 1, -1):
                if boxes[j][0] != last:
                    c += 1
                    last = boxes[j][0]
                
            # print("f", k, j, c)
            return c

        stack = deque()
        stack.append((-1, 0))
        #(i,dp[i])
        for i in range(n):
            #1.dp[i]从对首取出搬运次数最少的计算
            if len(stack) > 0:
                dp[i] = stack[0][1] + f(stack[0][0] + 1,i)
            #2.dp[i]进入队尾，将大于dp[i]的出栈
            while len(stack) > 0 and stack[-1][1] >= dp[i]:
                stack.pop()
            stack.append((i, dp[i]))
            #3.队首中重量超过maxWeight的出栈
            while len(stack) > 0 and i < n - 1:
                if pre[i+2] - pre[stack[0][0] + 1] > maxWeight or i - stack[0][0] + 1 > maxBoxes:
                    stack.popleft()
                else:
                    break 
            # print(dp, stack)
        return dp[n-1]
    
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        dp = [2 * (i + 1) for i in range(n)]
        pre = [0] * (n + 1)
        for i,v in enumerate(boxes):
            pre[i + 1] = pre[i] + v[1]

        #前缀和
        cost = [0] * (n + 1)
        for i in range(1,n):
            if boxes[i][0] != boxes[i-1][0]:
                cost[i] = cost[i-1] + 1
            else:
                cost[i] = cost[i-1]

        def f(k,i):
            return 1 + cost[i] - cost[k] + 1

        stack = deque()
        stack.append((-1, 0))
        #(i,dp[i])
        for i in range(n):
            #1.dp[i]从队首取出搬运次数最少的计算
            if len(stack) > 0:
                dp[i] = stack[0][1] + f(stack[0][0] + 1,i)
            #2.dp[i]进入队尾，将大于dp[i]的出栈
            while len(stack) > 0 and stack[-1][1] >= dp[i]:
                stack.pop()
            stack.append((i, dp[i]))
            #3.队首中重量超过maxWeight的出栈
            while len(stack) > 0 and i < n - 1:
                if pre[i+2] - pre[stack[0][0] + 1] > maxWeight or i - stack[0][0] + 1 > maxBoxes:
                    stack.popleft()
                else:
                    break 
            # print(dp, stack)
        return dp[n-1]

#14  
boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]]
portsCount = 5
maxBoxes = 5
maxWeight = 7

#4
# boxes = [[1,1],[2,1],[1,1]]
# portsCount = 2
# maxBoxes = 3
# maxWeight = 3

#6
# boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]]
# portsCount = 3
# maxBoxes = 6
# maxWeight = 7


sol = Solution()
print(sol.boxDelivering(boxes, portsCount, maxBoxes, maxWeight))
