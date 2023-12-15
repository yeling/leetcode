# auther yeling
from typing import List
from bisect import *
from collections import *

caseNum = int(input())
# TLE
for i in range(0, caseNum):
    n, c, d = [int(v) for v in input().split(' ')]
    quests = [int(v) for v in input().split(' ')]
    # print(quests)
    quests.sort(reverse=True)
    if c <= sum(quests[:d]):
        print('Infinity')
        continue
    if c > d * quests[0]:
        print('Impossible')
        continue
    k = 0
    pre = [0] * (n + 1)
    pre[0] = quests[0]
    for i in range(1,n):
        pre[i] = pre[i - 1] + quests[i]

    while k <= d:
        t = pre[min(k,n - 1)]
        tempSum = d // (k + 1) * t
        # print(n, min(d % (k + 1) - 1, n - 1))
        tempSum += pre[min(d % (k + 1) - 1, n - 1)]
        # print(t, tempSum, k)
        if tempSum < c:
            k -= 1
            break
        k += 1
    # while k <= d:
    #     t = sum(quests[:k+1])
    #     tempSum = d // (k + 1) * t
    #     tempSum += sum(quests[:d % (k + 1) ])
    #     # print(t, tempSum, k)
    #     if tempSum < c:
    #         k -= 1
    #         break
    #     k += 1
    print(k)
