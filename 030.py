##########################################
import io
import sys

_INPUT = """\
1 10
9 1



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,W = map(int,input().split())
w= [0]
v= [0]
for i in range(N):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)
dp = [[0 for i in range(110)] for j in range(100000)]
dp[0][0] = 0
for i in range(1,W+1):
    dp[0][i] = -10**9
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