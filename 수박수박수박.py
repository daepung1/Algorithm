def solution(n):
    answer = ''
    count=0
    for i in range(n):
        if count==0:
            answer=answer+"수"
            count=1
        else:
            count=0
            answer=answer+"박"
    return answer