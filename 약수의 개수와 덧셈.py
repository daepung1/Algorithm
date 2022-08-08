def solution(left, right):
    answer = 0
    check=[]
    for i in range(left,right+1):
        check=[]
        for l in range(1,i+1):
            if i%l==0:
                check.append(l)
        if len(check)%2==0:
            answer=answer+i
        else:
            answer=answer-i
    return answer

left=13
right=17
answer=0
check=[]
for i in range(left,right+1):
    check=[]
    for l in range(1,i+1):
        if i%l==0:
            check.append(l)
    if len(check)%2==0:
        answer=answer+i
    else:
        answer=answer-i
print(answer)