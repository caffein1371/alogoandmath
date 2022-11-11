##########################################
import io
import sys

_INPUT = """\
13
243 156 104 280 142 286 196 132 128 195 265 300 130


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
thou = 1000
ans = 0
import itertools
ans= 0
for i in itertools.combinations(Alist,5):
    if sum(i)==1000:
        ans+=1
print (ans)
