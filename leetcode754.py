
# auther yeling
from typing import List
import math
# 60 / 73 个通过的测试用例
class Solution:
    def reachNumber(self, target: int) -> int:
        if target < 0:
            target = -target 
        begin = math.floor(math.sqrt(2 * target)) - 1
        sum = (begin + 1) * begin / 2
        while sum != target:
            begin += 1
            sum += begin
            if sum > target and (sum - target)%2 == 0:
                break
        return begin

sol = Solution()


print(sol.reachNumber(6))
print(sol.reachNumber(8))
print(sol.reachNumber(759))