import random
import sys
from math import gcd, lcm, sqrt, isqrt, perm, comb, factorial
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce, cmp_to_key
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from copy import deepcopy
from bisect import bisect_left, bisect_right
from string import ascii_lowercase, ascii_uppercase
inf = float('inf')
input = lambda: sys.stdin.readline().strip()
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
MOD = 10**9+7

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def solve():
    n = II()
    g = [[] for _ in range(n)]
    cnt = [0]*n
    for _ in range(n-1):
        u, v = GMI()
        g[u].append(v)
        g[v].append(u)

    @bootstrap
    def dfs(u, fa):
        if len(g[u]) == 1 and u != 0:
            cnt[u] = 1
            yield
        for v in g[u]:
            if v != fa:
                yield dfs(v, u)
                cnt[u] += cnt[v]
        yield

    dfs(0, -1)

    q = II()
    for _ in range(q):
        x, y = GMI()
        res = cnt[x]*cnt[y]
        print(res)
    return

for _ in range(int(input())):
    solve()
