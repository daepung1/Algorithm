def solution(arr):
    temp=12345
    answer=[]
    for i in range(len(arr)):
        if temp==arr[i]:
            arr[i]=arr[i]
        else:
            answer.append(arr[i])
        temp=arr[i]
    
    return answer
arr=[1,1,3,3,0,1,1]
temp=12345
answer=[]
for i in range(len(arr)):
    if temp==arr[i]:
        arr[i]=arr[i]
    else:
        answer.append(arr[i])
    temp=arr[i]
print(answer)