def solution(a, b):
    d=len(a)
    answer = 0
    for i in range(d):
        answer=answer+(a[i]*b[i])
    return answer