##########################################
import io
import sys

_INPUT = """\
6
30 10 60 10 60 50


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))

ans = 0
dp = [0 for i in range(N)]
dp[0]=0
dp[1]=abs(Alist[1]-Alist[0])
for i in range(2,len(Alist)):
    dp[i] = min(dp[i-1]+abs(Alist[i]-Alist[i-1]),dp[i-2]+abs(Alist[i]-Alist[i-2]))

#print (dp)
print (dp[-1])