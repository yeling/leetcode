
# auther yeling
from typing import List
from bisect import *
from collections import *
from functools import *
from itertools import *

MOD = 10 ** 9 + 7

class Solution:
    def pyramidTransition2(self, bottom: str, allowed: List[str]) -> bool:
        cache = defaultdict(list)
        for v in allowed:
            cache[v[0:2]].append(v[2])
        # print(cache)
        def dfs(b, index, pre):
            # print(b, index, pre)
            if len(b) == 1:
                return True
            if index == len(b) - 1:
                return dfs(pre,0,'')
            
            arr = cache[b[index:index + 2]]
            for v in arr:
                ret = dfs(b, index + 1, pre + v)
                if ret:
                    return ret
            
            return False
            
        return dfs(bottom, 0, '')

    #记忆化搜索
    def pyramidTransition3(self, bottom: str, allowed: List[str]) -> bool:
        cache = defaultdict(list)
        for v in allowed:
            cache[v[0:2]].append(v[2])
        def getProduct(pair):
            stack = deque()
            stack.append([])
            for i in range(len(pair)):
                count = len(stack)
                for _ in range(count):
                    src = stack.popleft()
                    for v in pair[i]:
                        dst = src[0:]
                        dst.append(v)
                        stack.append(dst)
            return list(stack)
            
        # print(cache)
        fc = defaultdict(str)
        @lru_cache(maxsize=None)
        def dfs(b):
            if b in fc:
                return fc[b]
            if len(b) == 1:
                fc[b] = True
                return True
            p = []
            for i in range(1,len(b)):
                
                arr = cache[b[i-1:i+1]]
                if arr == None:
                    fc[b] = False
                    return False
                else:
                    p.append(arr)
            # print(p)
            allproduct = getProduct(p)
            for v in allproduct:
                v = ''.join(v)
                ret = dfs(v)
                if ret:
                    fc[b] = True
                    return True
            fc[b] = False
            return False
        return dfs(bottom)
    
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        m = defaultdict(list)
        for allow in allowed:
            m[allow[:2]].append(allow[2])

        @lru_cache(maxsize=None)
        def helper(s):
            p = []
            for i in range(1, len(s)):
                chs = m[s[i - 1] + s[i]]
                if len(chs) == 0: return False
                p.append(chs)
            if len(p) == 1: return True
            for chs in product(*p):
                if helper("".join(chs)):
                    return True
            return False
        return helper(bottom)

sol = Solution()
# bottom = "BCD"
# allowed = ["BCC","CDE","CEA","FFF"]
bottom = "AAAA"
allowed = ["AAB","AAC","BCD","BBE","DEF"]
print(sol.pyramidTransition(bottom, allowed))
