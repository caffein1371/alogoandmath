##########################################
import io
import sys

_INPUT = """\
5
3 1 4 1 5

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
print (sum(Alist))