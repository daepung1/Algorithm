def solution(n, lost, reserve):
   
    reserve=sorted(list(set(reserve)))
    lost=sorted(list(set(lost)))
    lost2 = [i for i in lost if i not in reserve]
    reserve2 = [i for i in reserve if i not in lost]
    m=len(reserve2)
    t=len(lost2)

    c=n-t
    for i in range(m):
        for l in range(t):
            if lost2[l]-1==reserve2[i] or lost2[l]+1==reserve2[i]:
                c=c+1
                lost2[l]=-1
                reserve2[i]=-1
    answer = c
    return answer
n=5
lost=[2,7,1,4,4,5,1]
reserve=[1,4]

reserve=sorted(list(set(reserve)))
lost=sorted(list(set(lost)))
print("정렬",reserve)
print("정렬",lost)

lost2 = [i for i in lost if i not in reserve]
reserve2 = [i for i in reserve if i not in lost]    
m=len(reserve2)
t=len(lost2)
print("정석",reserve2)
print("정석",lost2)
for i in reserve:
    if i in lost:
        print("i",i)
        reserve.remove(i)
        lost.remove(i)
print("틀림",reserve)
print("틀림",lost)
c=n-t
for i in range(m):  
    for l in range(t):
        if lost[l]-1==reserve[i] or lost[l]+1==reserve[i]:
            c=c+1
            lost[l]=-5
            reserve[i]=-9

            

