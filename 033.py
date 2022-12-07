##########################################
import io
import sys

_INPUT = """\
1000000000 1000000000
-1000000000 -1000000000
0 -1000000000




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
ax,ay = map(int,input().split())
bx,by = map(int,input().split())
cx,cy = map(int,input().split())

BAx = (ax-bx)
BAy = (ay-by)
BCx = (cx-bx)
BCy = (cy-by)
CAx = (ax-cx)
CAy = (ay-cy)
CBx = (bx-cx)
CBy = (by-cy)

pattern = 2
if BAx*BCx+BAy*BCy<0:
    pattern =1
if CAx*CBx+CAy*CBy<0:
    pattern =3

import math
ans = 0
if pattern ==1:
    ans = math.sqrt(BAx*BAx+BAy*BAy)
elif pattern ==3:
    ans = math.sqrt(CAx*CAx+CAy*CAy)
elif pattern ==2:
    S = abs(BAx*CAy-BAy*CAx)
    BClength = math.sqrt(BCx*BCx+BCy*BCy)
    ans = S/BClength

print (ans)