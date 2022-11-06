##########################################
import io
import sys

_INPUT = """\
2 8 8


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C = map(int,input().split())
print (A*B*C)