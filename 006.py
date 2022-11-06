##########################################
import io
import sys

_INPUT = """\
100


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
print (2*N+3)