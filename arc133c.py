# auther yeling
from typing import List
from bisect import *
from collections import *

# 累加行需要减小的数量，列需要减小的数量
# 

def main(m,n,k,a,b):
    sa, sb = 0, 0
    for v in a:
        sa += (n * (k - 1) - v)%k
    for v in b:
        sb += (m * (k - 1) - v)%k
    if sb % k != sa % k :
        print(-1)
    else:
        print(n * m * (k - 1) - max(sa,sb))
    
m,n,k = [int(v) for v in (input()).split(' ')]
a = [int(v) for v in (input()).split(' ')]
b = [int(v) for v in (input()).split(' ')]

main(m,n,k,a,b)

