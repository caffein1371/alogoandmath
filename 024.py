##########################################
import io
import sys

_INPUT = """\
2
2 50
4 100

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
PQ = []
for i in range(N):
    P,Q = map(int,input().split())
    PQ.append([P,Q])
ans = 0
for i in range(N):
    ans+=1/PQ[i][0]*PQ[i][1]
print (ans)
