##########################################
import io
import sys

_INPUT = """\
10 5
8 6 9 1 2 1 10 100 1000 10000
2 3
1 4
3 9
6 8
1 10


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,Q = map(int,input().split())
Alist = list(map(int,input().split()))
templist = [0 for i in range(10**5+1)]
sum = 0
for i in range(len(Alist)):
    templist[i] = Alist[i]+sum
    sum = templist[i]
LR = []

for i in range(Q):
    l,r = map(int,input().split())
    print (templist[r-1]-templist[l-1]+Alist[l-1])


