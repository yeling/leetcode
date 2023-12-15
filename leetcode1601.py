
# auther yeling
# 1601. 最多可达成的换楼请求数目
# 遍历所有的请求
from typing import List
from bisect import *

MOD = 10 ** 9 + 7


class Solution:
    # dfs
    def maximumRequests2(self, n: int, requests: List[List[int]]) -> int:
        build = [0 for _ in range(n)]
        global res, c
        res = 0
        c = 0

        def dfs(index, preLen, build):
            global res, c
            c += 1
            # print('dfs', c , index, preLen, build)
            count = 0
            for v in build:
                if v == 0:
                    count += 1
            if count == len(build):
                res = max(res, preLen)

            if index == len(requests):
                return
            curr = requests[index]
            # do nothing
            dfs(index + 1, preLen, build)
            # select
            build[curr[0]] -= 1
            build[curr[1]] += 1
            dfs(index + 1, preLen + 1, build)
            build[curr[0]] += 1
            build[curr[1]] -= 1

            return

        dfs(0, 0, build)
        return res

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m = len(requests)
        res = 0
        build = [0 for _ in range(n)]
        for i in range(1, 1 << m):
            bitcount = bin(i).count('1')
            if bitcount < res:
                continue
            for k in range(n):
                build[k] = 0
            for j in range(m):
                if i & (1 << j):
                    build[requests[j][0]] -= 1
                    build[requests[j][1]] += 1
            count = 0
            for v in build:
                if v == 0:
                    count += 1
            if all(x == 0 for x in build):
                res = bitcount

        return res
    
    


n = 5
requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
n = 4
requests = [[0, 3], [3, 1], [1, 2], [2, 0]]

# n = 3
# requests = [[1, 2], [1, 2], [2, 2], [0, 2], [2, 1], [1, 1], [1, 2]]
# 4

n = 3
requests = [[0, 0], [1, 1], [0, 0], [2, 0],
            [2, 2], [1, 1], [2, 1], [0, 1], [0, 1]]
# 5

sol = Solution()
print(sol.maximumRequests2(n, requests))
print(sol.maximumRequests(n, requests))
