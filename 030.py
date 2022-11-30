##########################################
import io
import sys

_INPUT = """\
6 15
6 5
5 6
6 4
6 6
3 5
7 2



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,W = map(int,input().split())
w= [0]*(N+1)
v= [0]*(N+1)
for i in range(1,N+1):
    a,b = map(int,input().split())
    w[i]=a
    v[i]=b
#1つ目の配列が2つ目
dp = [[0 for i in range(W+1)] for j in range(N+1)]

for i in range(1,W+1):
    dp[0][i] = -1

for i in range(1,N+1):
    for j in range(W+1):
        #j<w[i]の時、次の商品を選べない
        if (j<w[i]):
            dp[i][j] = dp[i-1][j]
        #j>=W[i]の時は選ぶことも選ばないこともできる
        if (j>=w[i]):
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
        #print (dp[i][j])
ans = 0
for i in range(W+1):
    ans = max(ans,dp[N][i])
print (ans)