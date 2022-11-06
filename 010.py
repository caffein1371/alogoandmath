##########################################
import io
import sys

_INPUT = """\
5

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
ans = 1
for i in range(1,N+1):
    ans*=i

print (ans)

