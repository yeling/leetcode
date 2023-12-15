# auther yeling
from typing import List
from collections import *
import math

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        sets = [{i,} for i in range(1, n + 1)]
        for i in range(n):
            a = list(map(int, input()))
            for j in range(n):
                if a[j] == 1:
                    sets[j].update(sets[i])
        for i in range(n):
            print(len(sets[i]), *sets[i])

main()
   
