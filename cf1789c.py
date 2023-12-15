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

mi = lambda :map(int,input().split())
li = lambda :list(mi())

def main2(n, m, nums, ops):
    # print(n, m, nums, ops)
    cnt = defaultdict(int)
    for v in nums:
        cnt[v] += 1
    for p,v in ops:
        nums[p - 1] = v
        for cv in nums:
            cnt[cv] += 1
    ans = 0
    for k in cnt:
        ans += cnt[k] * (m + 1 - cnt[k] ) + cnt[k] * (cnt[k] - 1)//2
        # print(k, ans)
    # print(cnt, ans)
    print(ans)
    return 

def main(n, m, nums, ops):
    # print(n, m, nums, ops)
    # 计算每个数字出现的次数
    cnt = defaultdict(int)
    # 计算上一个数字出现的时间
    pre = defaultdict(int)
    for v in nums:
        pre[v] = 1

    for i,[p,v] in enumerate(ops):
        # i + 2
        cnt[nums[p - 1]] += i + 2 - pre[nums[p - 1]]
        pre[nums[p - 1]] = i + 2

        nums[p - 1] = v
        pre[v] = i + 2

        if i == m - 1:
            for cv in nums:
                cnt[cv] += i + 2 - pre[cv] + 1
    # print(cnt)
    ans = 0
    for k in cnt:
        ans += cnt[k] * (m + 1 - cnt[k] ) + cnt[k] * (cnt[k] - 1)//2
        # print(k, ans)
    # print(cnt, ans)
    print(ans)
    return 

caseNum = int(input())
for i in range(0, caseNum):
    n,m = li()
    nums = li()
    ops = []
    for j in range(m):
        ops.append(li())
    main(n, m, nums, ops)

   
