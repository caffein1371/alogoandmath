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

for i in range(2,int(math.sqrt(N))+1):
    
