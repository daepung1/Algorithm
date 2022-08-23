def solution(seoul):
    s=''
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            s=i
            break
    
    answer = "김서방은 "+ str(s) +"에 있다"
    return answer