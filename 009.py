##########################################
import io
import sys

_INPUT = """\
3 11
2 5 9

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,S = map(int,input().split())
Alist = list(map(int,input().split()))
import itertools

for i in range(1,N+1):
    for v in itertools.combinations(Alist,i):
        if sum(v)==S:
            print ("Yes")
            quit()
print ("No")