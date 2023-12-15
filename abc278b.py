# auther yeling
from typing import List
import math

def isConfuse(h, m):
    hstr, mstr = str(h), str(m)
    if(h <= 9):
        hstr = '0' + str(h)
    if(m <= 9):
        mstr = '0' + str(h)
    nh = hstr[0] + mstr[0]
    nm = hstr[1] + mstr[1]
    if int(nh) >= 24 or int(nm) >= 60:
        return False
    
    return True

h, m  = [int(v) for v in (input()).split(' ')]
# h , m = 20, 40
while True:
    if isConfuse(h,m):
        print(h,m)
        break
    m += 1
    if m == 60:
        m = 0
        h+=1
    if h == 24:
        h = 0

    

