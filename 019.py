##########################################
import io
import sys

_INPUT = """\
6
1 3 2 1 1 2

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))

def per(n):
    return n*(n-1)//2

import collections
ans=0
c = collections.Counter(Alist)
a = [1,2,3]
temp = [0,0,0]

for i in range(len(a)):
    temp[i] = c[a[i]]
    #print (temp[i])

ans = 0
for i in range(3):
    ans+= per(temp[i])
print (ans)