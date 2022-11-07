##########################################
import io
import sys

_INPUT = """\
827847039317

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
ans = []
import math

for i in range(1,int(math.sqrt(N))+1):
    if N%i==0:
        ans.append(i)
        ans.append(N//i)
for i in ans:
    print (i)