def solution(n):
    if n==2:
        answer=1
    elif n==3:
        answer=3
    else:
        answer=2
        for i in range(4,n+1):
            for l in range(2,n):
                if i<=l:
                    break
                if i%l !=0:
                    if l==i-1:
                        answer=answer+1
                    else:
                        l=l
                else:
                    break
        
    
    return answer
temp=[2,3]
n=15
for i in range(4,n+1):
    for l in range(2,n):
        if i<=l:
            break
        if i%l !=0:
            if l==i-1:
                temp.append(i)
            else:
                l=l
        else:
            break
if n==2:
    temp=[2]
elif n==3:
    temp=[2,3]

print(temp)