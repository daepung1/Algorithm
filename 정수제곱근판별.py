import math

def solution(n):
    answer = 0
    m=str(math.sqrt(n))
    d=0
    if m[-1]=='0':
        d=math.sqrt(n)+1
        answer=d*d
    else:
        answer=-1
    return answer
n=121
m=str(math.sqrt(n))
d=0
if m[-1]=='0':
    d=math.sqrt(n)+1
    answer=d*d
else:
    answer=-1