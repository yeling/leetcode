
# auther yeling
from typing import List
import math
import string
from collections import deque 

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m,  n = len(grid) ,len(grid[0])
        start = [0,0]
        keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    start = [i,j]
                elif grid[i][j].islower():
                    keys += 1
        # print("%s %s"%(start, keys))
        #[x, y, mask]
        stack = deque([(start[0], start[1], 0)])
        dirs = [[1,0], [-1,0],[0,1],[0,-1]]
        cache = dict()
        cache[(start[0], start[1], 0)] = 0
        dstKeys = 1
        for i in range(keys):
            dstKeys = dstKeys | (1 << i)

        # print(dstKeys)

        while len(stack) > 0 :
            cur = stack.popleft()
            # print(cur)
            for dx, dy in dirs:
                nx = cur[0] + dx
                ny = cur[1] + dy
                dis = cache[cur]
                if nx >= 0 and nx < m and ny >= 0 and ny < n and grid[nx][ny] != '#':
                    if grid[nx][ny] == '.' or grid[nx][ny] == '@':
                        if (nx, ny, cur[2]) not in cache:
                            cache[(nx, ny, cur[2])] = dis + 1
                            stack.append((nx, ny, cur[2]))
                    elif grid[nx][ny].islower():
                        next = (nx, ny, cur[2] | (1 << (ord(grid[nx][ny]) - 97)))
                        if next not in cache:
                            cache[next] = dis + 1
                            if next[2] == dstKeys:
                                return dis + 1
                            stack.append(next)
                    else :
                        if cur[2] & (1 << (ord(grid[nx][ny].lower()) - 97)) and (nx, ny, cur[2]) not in cache:
                            cache[(nx, ny, cur[2])] = dis + 1
                            stack.append((nx, ny, cur[2]))
        return -1
    



    
    
sol = Solution()
grid = ["@.a..","###.#","b.A.B"]
grid = ["@fedcbBCDEFaA"]
grid = ["@bBaA"]
print(sol.shortestPathAllKeys(grid))

# print(string.ascii_lowercase)
# print(ord('a'))


def quickPow(a, n):
    ans = 1
    while(n > 0):
        if n & 1 == 1:
            ans = ans * a
        a = a * a
        n = n >> 1
    return ans

def quickPowMode(a, n, p):
    ans = 1
    while(n > 0):
        if n & 1 == 1:
            ans = ans * a % p
        a = a * a % p
        n = n >> 1
    return ans % p

# print(quickPow(2,10))
# print(quickPowMode(2,10, 7))

