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

def main(matrix):
    # print(matrix)
    stack = deque()
    stack.append(matrix[0][0])
    stack.append(matrix[0][1])
    stack.append(matrix[1][1])
    stack.append(matrix[1][0])

    # print(stack)
    ans = False
    for i in range(4):
        if stack[(0 + i)%4] < stack[(1 + i)%4] and stack[(3 + i)%4] < stack[(2 + i)%4] \
            and stack[(0 + i)%4] < stack[(3 + i)%4] and stack[(1 + i)%4] < stack[(2 + i)%4]:
            ans = True
    if ans:
        print("Yes")
    else:
        print("No")
    return 

# matrix = [[1,3],[5,7]]
# main(matrix)

caseNum = int(input())
for i in range(0, caseNum):
    matrix = [li(),li()]
    main(matrix)
   
