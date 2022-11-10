##########################################
import io
import sys

_INPUT = """\
5
100 300 400 400 200

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))

import collections
ans=0
#100+400
#200+300の組み合わせはいくつあるかを調べれば良い
c = collections.Counter(Alist)
a = [100,200,300,400]
temp = [0,0,0,0]
for i in range(len(a)):
    temp[i] = c[a[i]]
    #print (temp[i])
print (temp[0]*temp[3]+temp[1]*temp[2])