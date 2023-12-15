from typing import List

INF = 10 ** 6

class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
      g = [[INF]*n for _ in range(n)]
      for u,v,w in roads:
        g[v][u] = g[u][v] = min(g[u][v], w)
      for i in range(n):
        g[i][i] = 0

      def floyd(flag):
        dp = [g[i][:] for i in range(n)]        
        ret = 0
        for k in range(n):
          if flag[k] == False:
            continue
          for i in range(n):
            if flag[i] == False:
              continue
            for j in range(n):
              if flag[j] == False:
                continue
              dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
        for i in range(n):
          for j in range(i + 1,n):
            if flag[i] and flag[j]:
              ret = max(ret, dp[i][j])
        # print(flag, dp)
        return ret 

      ans = 1
      for state in range(1, 2 ** n):
        flag = [False] * n
        for i in range(n):
          if (state >> i) & 1 != 0:
            flag[i] = True
        curr = floyd(flag)        
        if curr <= maxDistance:
          ans += 1
        # print(state, flag, curr, ans)
      return ans

n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]
sol = Solution()
print(sol.numberOfSets(n, maxDistance, roads))

