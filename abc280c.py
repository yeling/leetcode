# auther yeling
from typing import List
from bisect import *
from collections import *


def main(s, t):
    n = len(s)
    for i in range(n):
        if s[i] != t[i]:
            print(i+1)
            return
    print(n + 1)
    


s = input()
t = input()
main(s,t)

