##########################################
import io
import sys

_INPUT = """\
33 88


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B = map(int,input().split())
import math

print (math.gcd(A,B))