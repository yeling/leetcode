# auther yeling
from typing import List
import math

def main(n, nums):
    f = ['H', 'D', 'C', 'S']
    s = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    cache = set()
    for item in nums:
        if item[0] in f and item[1] in s:
            if item in cache:
                print('No')
                return 
            cache.add(item)
            continue
        else:
            print('No')
            return 
    print('Yes')

n = int(input())
nums = []
for _ in range(n):
    nums.append(input())
main(n, nums)

