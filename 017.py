##########################################
import io
import sys

_INPUT = """\
3
12 18 14

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))

import math

ans = Alist[0]
for i in range(1,len(Alist)):
    #print (i)
    ans = ans*Alist[i]//math.gcd(ans,Alist[i])
print (ans)
