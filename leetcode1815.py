
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
    # 52 / 74
    # 61 / 74 
    def maxHappyGroups2(self, batchSize: int, groups: List[int]) -> int:
        ans = 0
        cache = defaultdict(int)
        for i,v in enumerate(groups):
            groups[i] = groups[i]%batchSize
        # print(groups)
        for v in groups:
            if v%batchSize == 0:
                ans += 1
            else:
                cache[v%batchSize] += 1
        print(cache)
        for i in range(1,batchSize):
            for v in combinations(list(range(batchSize - 1)), i):
                add = [0] * (len(v) + 1)
                cacheAdd = defaultdict(int)
                for i,k in enumerate(v):
                    if i == 0:
                        add[i] = v[i] + 1
                    else:
                        add[i] = v[i] - v[i - 1]
                    cacheAdd[add[i]] += 1
                add[len(v)] = batchSize - 1 - v[len(v) - 1]
                cacheAdd[add[-1]] += 1

                curr = INF
                for m in cacheAdd:
                    if cache[m] > 0:
                        curr = min(curr, cache[m]//cacheAdd[m])
                    else:
                        curr = 0
                        break
                if curr > 0 and m != INF:
                    ans += curr
                    for m in add:
                        cache[m] -= curr
                        if cache[m] == 0:
                            del cache[m]

                # print(v, add, ans)
        tempSum = 0
        for v in cache:
            tempSum += cache[v]
        if tempSum > 0:
            ans += 1
     
        return ans
    #状态压缩，需要枚举所有状态
    #记忆化搜索
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        cnt = [0] * batchSize
        # for i,v in enumerate(groups):
        #     groups[i] = groups[i]%batchSize
        # print(groups)
        for v in groups:
            cnt[v%batchSize] += 1
        print(cnt)

        @cache
        def dfs(left: int, state: tuple[int]) -> int:
            res = 0
            curr = list(state)
            for i,v in enumerate(curr):
                if v:
                    curr[i] -= 1
                    res = max(res, (left == 0) + dfs((left + i + 1)%batchSize, tuple(curr)))
                    curr[i] += 1
            return res
        return cnt[0] + dfs(0,tuple(cnt[1:]))
    
    def maxHappyGroups3(self, m: int, groups: List[int]) -> int:
        cnt = [0] * m
        for x in groups:
            cnt[x % m] += 1

        @cache  # 记忆化
        def dfs(left: int, cnt: tuple[int]) -> int:
            res = 0
            cnt = list(cnt)
            for x, c in enumerate(cnt):  # 枚举顾客
                if c:  # cnt[x] > 0
                    cnt[x] -= 1
                    res = max(res, (left == 0) + dfs((left + x + 1) % m, tuple(cnt)))  # x 从 0 开始，这里要 +1
                    cnt[x] += 1
            return res
        return cnt[0] + dfs(0, tuple(cnt[1:]))  # 转成 tuple 这样能记忆化

    
batchSize = 4
groups = [1,3,2,5,2,2,1,6]
# batchSize = 3
# groups = [1,2,3,4,5,6]
# groups = [369821235,311690424,74641571,179819879,171396603,274036220]
sol = Solution()
print(sol.maxHappyGroups(batchSize, groups))
print(sol.maxHappyGroups3(batchSize, groups))
