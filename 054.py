##########################################
import io
import sys

_INPUT = """\
876543210987654321

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(N):
    if N ==1 or N==2:
        return 1
    else:
        return fib(N-1)+fib(N-2)
N = int(input())
print (fib(N)%10**9)

