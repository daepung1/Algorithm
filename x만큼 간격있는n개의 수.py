def solution(x, n):
    answer=[]
    c=x
    for i in range(n):
        answer.append(x)
        x=x+c
    
    return answer