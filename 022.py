##########################################
import io
import sys

_INPUT = """\
6
40000 50000 20000 80000 50000 30000

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
#Alist = sorted(Alist)
thou=100000
ans = 0
import bisect
import collections
c = collections.Counter(Alist)

for i in range(N):
    a= c[Alist[i]]
    temp = thou-Alist[i]
    b = c[temp]
    if Alist[i]!=temp:
        ans+=a*b/2
    else:
        ans+=a*b/4
print (ans)    

