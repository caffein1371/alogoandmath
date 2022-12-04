##########################################
import io
import sys

_INPUT = """\
7 18
7 2
1 6
5 2
1 3
7 6
5 3
5 6
5 4
1 7
2 6
3 4
5 1
4 7
4 6
5 7
3 2
4 2
1 4







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
A = []
B = []
from collections import defaultdict
d = defaultdict(list)
for i in range(M):
    a,b = map(int,input().split())
    d[a].append(b)
    d[b].append(a)
ans = 0
#print (d)
for i in d:
    temp = 0
    for j in d[i]:
        if j<i:
            temp+=1
            #print (i,j)
    if temp==1:
        ans+=1
print(ans)



