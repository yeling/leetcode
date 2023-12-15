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

def main2(n, k, nums, cold, hot):
    cpu1 = -1
    cpu1T = 0
    cpu2 = -1
    cpu2T = 0
    ans = 0
    for i,v in enumerate(nums):
        if cpu1 == -1:
            cpu1 = v
            cpu1T += cold[v-1]
            ans += cold[v-1]
        elif cpu2 == -1:
            if cpu1 == v:
                if cpu1T + hot[v-1] < cpu2T + hot[v-1]:
                    cpu1 = v
                    cpu1T += hot[v-1]
                    ans += hot[v-1]
                else:
                    cpu2 = v
                    cpu2T += hot[v-1]
                    ans += hot[v-1]
            else:
                cpu2 = v
                cpu2T += cold[v-1]
                ans += cold[v-1]
        elif cpu1 == v:
            if cpu2 == v:
                if cpu1T + hot[v-1] < cpu2T + hot[v-1]:
                    cpu1 = v
                    cpu1T += hot[v-1]
                    ans += hot[v-1]
                else:
                    cpu2 = v
                    cpu2T += hot[v-1]
                    ans += hot[v-1]
            elif cpu1T + hot[v-1] < cpu2T + cold[v-1]:
                cpu1 = v
                cpu1T += hot[v-1]
                ans += hot[v-1]
            else:
                cpu2 = v
                cpu2T += cold[v-1]
                ans += cold[v-1]
        elif cpu2 == v:
            if cpu1 == v:
                if cpu2T + hot[v-1] < cpu1T + hot[v-1]:
                    cpu2 = v
                    cpu2T += hot[v-1]
                    ans += hot[v-1]
                else:
                    cpu1 = v
                    cpu1T += hot[v-1]
                    ans += hot[v-1]
            elif cpu2T + hot[v-1] < cpu1T + cold[v-1]:
                cpu2 = v
                cpu2T += hot[v-1]
                ans += hot[v-1]
            else:
                cpu1 = v
                cpu1T += cold[v-1]
                ans += cold[v-1]
        else:
            if cpu2T + cold[v-1] < cpu1T + cold[v-1]:
                cpu2 = v
                cpu2T += cold[v-1]
                ans += cold[v-1]
            else:
                cpu1 = v
                cpu1T += hot[v-1]
                ans += hot[v-1]
        print(ans, cpu1, cpu1T, cpu2, cpu2T)

    print(ans)

    return 

def main(n, k, nums, cold, hot):
    cpu1 = -1
    cpu1T = 0
    cpu2 = -1
    cpu2T = 0
    ans = 0
    for i,v in enumerate(nums):
        if cpu1 == -1:
            cpu1 = v
            ans += cold[v-1]
        elif cpu2 == -1:
            if cpu1 == v:
                ans += hot[v-1]
            else:
                cpu2 = v
                ans += cold[v-1]
        elif cpu1 == v:
            ans += hot[v-1]
        elif cpu2 == v:
            ans += hot[v-1]
        else:
            cpu1 = v
            ans += cold[v-1]

    print(ans)     
    return 

# n = 5 
# k = 2
# nums = [2, 1, 2, 1, 1]
# cold = [65, 45]
# hot = [54, 7]
# main(n, k, nums, cold, hot)



caseNum = int(input())
for i in range(0, caseNum):
    n,k = li()
    nums = li()
    cold = li()
    hot = li()
    main(n, k, nums, cold, hot)

