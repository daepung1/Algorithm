def solution(n):
    answer=''
    n=str(n)
    n=sorted(n, reverse=True)
    for i in n:
        answer=answer+i
    answer=int(answer)
    return answer

n=123456
answer=''
n=str(n)
n=sorted(n, reverse=True)
for i in n:
    answer=answer+i
answer=int(answer)