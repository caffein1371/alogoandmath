##########################################
import io
import sys

_INPUT = """\
5
3 1 4 1 5
9 2 6 5 3

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
ans =0
for i in range(N):
    ans+=2/6*Alist[i]+4/6*Blist[i]
print(ans)