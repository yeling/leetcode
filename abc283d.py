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
YES="Yes"
NO="No"

mi = lambda :map(int,input().split())
li = lambda :list(mi())


def main(s):
    # print(s)
    n = len(s)
    good = [-1]*n
    stack = []
    pre = [[0] * 26 for _ in range(n)]
    for i,v in enumerate(s):
        if i > 0:
            pre[i] = pre[i - 1][:]

        if v == '(':
            stack.append(i)
        elif v == ')':
            good[i] = stack.pop()
        else:
            pre[i][ord(v) - 97] += 1

    curr = set()
    for i,v in enumerate(s):
        if v == '(':
            continue
        elif v == ')':
            diff = [pre[i][k] - pre[good[i]][k] for k in range(26)]
            for j in range(26):
                temp = chr(97 + j)
                if diff[j] > 0 and temp in curr:
                    curr.remove(temp)
        else:
            if v in curr:
                print(NO)
                return 
            else:
                curr.add(v)
    print(YES)
    # print(good, pre)


# s = '((a)ba)'
# main(s)

# curr = set()
# curr.remove('a')

s = input()
main(s)

