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

def fib(n):
    if n ==1 or n==2:
        return 1
    
    return fib(n-1)+fib(n-2)

N = int(input())
MOD = 10**9
print (fib(N)%MOD)

