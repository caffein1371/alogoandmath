##########################################
import io
import sys

_INPUT = """\
3
1 2 3
10 20 30

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Blist = list(map(int,input().split()))
Rlist = list(map(int,input().split()))

print (sum(Blist)/N+sum(Rlist)/N)