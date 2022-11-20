##########################################
import io
import sys

_INPUT = """\
4
0 1
2 0
2 3
3 1


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
import itertools
xy = []
for i in range(N):
    x,y = map(int,input().split())
    xy.append([x,y])

import math
ans = 10**15
for v in itertools.combinations(xy,2):
    ans = min(ans,math.sqrt((v[0][0]-v[1][0])**2+(v[0][1]-v[1][1])**2))

print (ans)

