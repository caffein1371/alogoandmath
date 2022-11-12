##########################################
import io
import sys

_INPUT = """\
6 2

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,R = map(int,input().split())
ans = 1
count = 1
for i in range(N,N-R,-1):
    ans*= i
for i in range(R):
    ans//=count
    count+=1

print (int(ans))