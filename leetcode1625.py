
# auther yeling
# 1625. 执行操作后字典序最小的字符串
from typing import List
from bisect import *
from collections import *

MOD = 10 ** 9 + 7

class Solution:
    #暴力枚举
    #TLE 65 / 80
    def findLexSmallestString2(self, s: str, a: int, b: int) -> str:
        
        s = [int(v) for v in s]
        n = len(s)
        pos = set()
        for j in range(1,10):
            if a * j%10 != 0:
                pos.add(a*j%10)
        print(pos)

        allMove = set()
        temp = 0
        while temp not in allMove:
            allMove.add(temp)
            temp = (temp + b)%n
        print(allMove)

        all = set()
        stack = deque()
        stack.append(''.join([str(v) for v in s]))
        # print(stack)
        while len(stack) > 0:
            l = len(stack)
            for _ in range(l):
                t = stack.popleft()
                #add
                for j in pos:
                    ne = [0] * n
                    for ki, v in enumerate(t):
                        v = int(v)
                        if ki%2 == 1:
                            ne[ki] = (v + j)%10
                        else:
                            ne[ki] = v
                    nestr = ''.join([str(v) for v in ne])
                    if nestr not in all:
                        all.add(nestr)
                        stack.append(nestr)
                #mv
                for mv in allMove:
                    ne = t[mv:] + t[:mv]
                    if ne not in all:
                        all.add(ne)
                        stack.append(ne)
        
        all = list(all)
        all.sort()
        print(len(all))
        # print(all)
        return all[0]
    
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        s = [int(v) for v in s]
        n = len(s)

        all = set()
        stack = deque()
        stack.append(''.join([str(v) for v in s]))
        # print(stack)
        while len(stack) > 0:
            l = len(stack)
            for _ in range(l):
                t = stack.popleft()
                #add
                ne = [0] * n
                for ki, v in enumerate(t):
                    v = int(v)
                    if ki%2 == 1:
                        ne[ki] = (v + a)%10
                    else:
                        ne[ki] = v
                nestr = ''.join([str(v) for v in ne])
                if nestr not in all:
                    all.add(nestr)
                    stack.append(nestr)
                #mv
                ne = t[b:] + t[:b]
                if ne not in all:
                    all.add(ne)
                    stack.append(ne)
        
        all = list(all)
        all.sort()
        # print(len(all))
        # print(all)
        return all[0]



sol = Solution()

s = "5525"
a = 9
b = 2
s = "74"
a = 5
b = 1

# s = "0011"
# a = 4
# b = 2

s = "43987654"
a = 7
b = 3
s ="059968036945394711795417294079643882545439101097287995561736161993252699"
a =7
b =11

print(sol.findLexSmallestString(s,a,b))
