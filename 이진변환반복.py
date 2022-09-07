def solution(s):
    count=0
    count_2=0
    answer=[]
    while(True):
        if s=="1":
            break
        a=''
        count_2=count_2+1
        print(s)
        for i in range(len(s)):
            if s[i]=="0":
                count=count+1
            else:
                a=a+"1"
        print(a)
        d=bin(len(a))
    
        d=d[2:]
        
        s=str(d)
        
    answer.append(count_2)
    answer.append(count)

    return answer

s="110010101001"	
count=0
count_2=0
while(True):
    if s=="1":
        break
    a=''
    count_2=count_2+1
    print(s)
    for i in range(len(s)):
        if s[i]=="0":
            count=count+1
        else:
            a=a+"1"
    print(a)
    d=bin(len(a))
   
    d=d[2:]
    
    s=str(d)
    
answer.append(count_2)
answer.append(count)
