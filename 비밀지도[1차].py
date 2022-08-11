def solution(n, arr1, arr2):
    arr1_2=[]
    arr2_2=[]
    str_temp=""
    temp=[]
    temp_len=0
    answer=[]
    for i in range(n):
        arr1_2.append(bin(arr1[i])[2:])
        arr2_2.append(bin(arr2[i])[2:])
    for i in range(n):
        if n!=len(arr1_2[i]):
            for l in range(n):
                arr1_2[i]="0"+arr1_2[i]
                temp_len=len(arr1_2[i])
                if temp_len==n:
                    break
    for i in range(n):
        if n!=len(arr2_2[i]):
            for l in range(n):
                arr2_2[i]="0"+arr2_2[i]
                temp_len=len(arr2_2[i])
                if temp_len==n:
                    break    
    for i in range(n):
        for l in range(n):
            if arr1_2[i][l]=="1" or arr2_2[i][l]=="1":
                str_temp=str_temp+"1"
            else:
                str_temp=str_temp+"0"
        temp.append(str_temp)
        str_temp=""
    for i in range(n):
        for l in range(n):
            if temp[i][l]=="1":
                str_temp=str_temp+"#"
            else:
                str_temp=str_temp+" "
        answer.append(str_temp)
        str_temp=""
    
    return answer

n=5
arr1=[9,20,28,18,11]
arr2=[30,1,21,17,28]
arr1_2=[]
arr2_2=[]
str_temp=""
temp=[]
temp_len=0
answer=[]
for i in range(n):
    arr1_2.append(bin(arr1[i])[2:])
    arr2_2.append(bin(arr2[i])[2:])
for i in range(n):
    if n!=len(arr1_2[i]):
        for l in range(n):
            arr1_2[i]="0"+arr1_2[i]
            temp_len=len(arr1_2[i])
            if temp_len==n:
                break
for i in range(n):
    if n!=len(arr2_2[i]):
        for l in range(n):
            arr2_2[i]="0"+arr2_2[i]
            temp_len=len(arr2_2[i])
            if temp_len==n:
                break    
print(arr1_2)
print(arr2_2)
for i in range(n):
    for l in range(n):
        if arr1_2[i][l]=="1" or arr2_2[i][l]=="1":
            str_temp=str_temp+"1"
        else:
            str_temp=str_temp+"0"
    temp.append(str_temp)
    str_temp=""
for i in range(n):
    for l in range(n):
        if temp[i][l]=="1":
            str_temp=str_temp+"#"
        else:
            str_temp=str_temp+" "
    answer.append(str_temp)
    str_temp=""
print(answer)