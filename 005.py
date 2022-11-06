##########################################
import io
import sys

_INPUT = """\
3
30 50 70

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
print (sum(Alist)%100)