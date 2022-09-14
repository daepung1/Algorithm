"""
옐로우는 중앙 브라운은 테두리를 감싸고 있다 브라운이 10 옐로우가 2라면
   ㅁㅁㅁㅁ
   ㅁㅇㅇㅁ  이런 모양인 셈이다
   ㅁㅁㅁㅁ   10 2
     
     ㅁㅁㅁ
     ㅁㅇㅁ  8 1
     ㅁㅁㅁ

    ㅁㅁㅁㅁㅁㅁㅁㅁ
    ㅁㅇㅇㅇㅇㅇㅇㅁ
    ㅁㅇㅇㅇㅇㅇㅇㅁ
    ㅁㅇㅇㅇㅇㅇㅇㅁ  24 24   
    ㅁㅇㅇㅇㅇㅇㅇㅁ
    ㅁㅁㅁㅁㅁㅁㅁㅁ
"""
def solution(brown, yellow):
    i=1
    answer=[]
    while(True):
        n=yellow/i
        if brown==(n+2)*2 + i*2:
            answer.append(int(n+2))
            answer.append(int((brown+yellow)/(n+2)))
            break 
        i=i+1
    return answer
yellow=24
brown=24
i=1
answer=[]
while(True):
    n=yellow/i
    if brown==(n+2)*2 + i*2:
        answer.append(int(n+2))
        answer.append(int((brown+yellow)/(n+2)))
        break 
    i=i+1
print(answer)

