def solution(d, budget):
    answer = 0
    i=0
    d=sorted(d)
    while(True):
        
        budget=budget-d[i]
        i=i+1
        if budget>=0:
            answer=answer+1
            
        if i>len(d)-1:
            break
        if budget<0:
            break
    return answer
d=[2,2,3,2]
budget=10
answer=0
i=0
d=sorted(d)
while(True):
    
    budget=budget-d[i]
    i=i+1
    if budget>=0:
        answer=answer+1
        
    if i>len(d)-1:
        break
    if budget<0:
        break
print(answer)