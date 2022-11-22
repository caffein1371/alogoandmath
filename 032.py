##########################################
import io
import sys

_INPUT = """\
8 3
1 2 3 3 4 5 6 7



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
import bisect
N,X = map(int,input().split())
Alist = list(map(int,input().split()))
Alist = sorted(Alist)
Alist = list(set(Alist))
ans = bisect.bisect(Alist,X)
if Alist[ans-1]==X:
    print ("Yes")
else:
    print ("No")
