##########################################
import io
import sys

_INPUT = """\
472249589291

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
import math

for i in range(2,int(math.sqrt(N)+1)):
    if N%i==0:
        print ("No")
        quit()

print ("Yes")