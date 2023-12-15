# auther yeling
from typing import List
from math import *

def main(n, m, nums):
    # print(n, m, nums)
    nums.sort(key=lambda x : x[1])
    g = n
    res = 0
    for v in nums:
        res += (g - gcd(g, v[0])) * v[1]
        g = gcd(g, v[0])
    if g == 1:
        print(res)
    else:
        print(-1)

    

allnums = [int(i) for i in (input()).split(' ')]
nums = []
for _ in range(allnums[1]):
    nums.append([int(i) for i in (input()).split(' ')])
main(allnums[0], allnums[1], nums)

