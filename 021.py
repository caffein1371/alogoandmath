##########################################
import io
import sys

_INPUT = """\
13
243 156 104 280 142 286 196 132 128 195 265 300 130


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
thou = 1000

ans= 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            for l in range(k+1,N):
                for m in range(l+1,N):
                    if Alist[i]+Alist[j]+Alist[k]+Alist[l]+Alist[m]==thou:
                        ans+=1
print (ans)
