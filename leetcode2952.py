from typing import List

INF = 10 ** 6

class Solution:    
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
      coins.sort()
      n = len(coins)
      ans = 0
      i = 0
      r = 0
      if coins[0] != 1:
        i = 0
        ans = 1
        r = 1
      else:
        r = 1
        i = 1
        ans = 0

      curr = 0
      while r < target:        
        while i < n and r >= coins[i] - 1:
          r += coins[i]
          i += 1

        if (i < n and r < coins[i] - 1) or r < target:
          curr = r + 1
          r = r + curr
          ans += 1
          # print(r, i, curr, ans)

      return ans

# coins = [1,4,10]
# target = 19

coins = [1,4,10,5,7,19]
target = 19

coins = [1,1,1]
target = 20

sol = Solution()
print(sol.minimumAddedCoins(coins, target))

