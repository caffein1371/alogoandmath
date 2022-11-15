##########################################
import io
import sys

_INPUT = """\
5

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
ans = 0

count = N
for i in range(1,N+1):
    ans+= 1*(N/i)

print (ans)
