# auther yeling
from typing import List
from bisect import *
from collections import *
from math import *

#1.获取所有质数因子
#2.计算可以容纳这些质因子的最大N
def getAllfactor(k):
    fac = []
    i = 2 
    y = k
    while i <= y:
        # print(i,y)
        if y % i == 0:
            fac.append(i)
            y = y // i
            i = 2
        elif i > sqrt(y):
            fac.append(y)
            break
        else:
            i += 1
    return fac
    
def main(k):
    mu = 1
    for i in range(2,k):
        mu *= i
        if mu%k == 0:
            print(i)
            return 


def main2(k):
    fac = getAllfactor(k)
    fac.sort()
    if fac[-1] == k:
        print(k)
        return 
    
    allFac = defaultdict(int)
    for v in fac:
        allFac[v] += 1
    
    n = int(sqrt(k)) + 1
    for i in range(2, k):
        temp = getAllfactor(i)
        # print(i, temp, allFac)
        for v in temp:
            if v in allFac:
                allFac[v] -= 1
                if allFac[v] == 0:
                    del allFac[v]
                if len(allFac) == 0:
                    print(i)
                    return     
    print(k)
    

def main3(K):
    mu = 1
    fac = getAllfactor(K)
    print(fac)
    d=defaultdict(int)
    for i in range(2,int(K**.5+1)):
        # print(i)
        while K%i==0:
            d[i]+=1
            K//=i
    print(d)
    ans=2
    for key,value in d.items():
        cnt=0
        while d[key]>0:
            cnt+=key
            cntcopy=cnt
            while cntcopy%key==0:
                cntcopy//=key
                d[key]-=1
        ans=max(ans,cnt)
    print(ans)
    

k = 123456789011
k = 40
# main(k)
# main2(k)
# main3(k)

print(getAllfactor(130))

# k = int(input())
# main(k)
# main2(k)

