##########################################
import io
import sys

_INPUT = """\
2


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
print (N+5)