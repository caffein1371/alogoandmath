##########################################
import io
import sys

_INPUT = """\
10

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())

import math

def check(n):
    ans = []
    for i in range(2,n+1):
        flag = True
        for j in range(2,i+1):
            print (i,j)
            if i%j!=0:
                flag = False
        if flag ==True:
            ans.append(i)
    return ans


count = 0

print (check(N))