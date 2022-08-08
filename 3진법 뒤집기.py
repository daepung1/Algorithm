def solution(n):
    answer = 0
    check=[]
    d=1
    while(True):
        m=n%3
        n=n//3
        check.append(m)
        if n<1:
            break
    check.reverse()
    for i in check:
        answer=answer+(i*d)
        d=d*3
    return answer
answer=0
n=45
check=[]
d=1
while(True):
    m=n%3
    n=n//3
    check.append(m)
    if n<1:
        break
check.reverse()
for i in check:
    answer=answer+(i*d)
    d=d*3
print(answer)