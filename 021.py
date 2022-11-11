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
ans = 0
#print (2**N)
#Nを2進数に変換したものを1bitずつ左へずらす
for i in range(1<<N):
    cost = 0
    #print (i)
    for j in range(N):
        if i>>j&1 ==1:
            cost+=Alist[j]
    if cost==thou:
        ans+=1

print (ans)
