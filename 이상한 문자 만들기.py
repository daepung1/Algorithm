def solution(s):
    answer=""
    check=0
    s="try hello world"
    for i in range(len(s)):
        if s[i]==" ":
            answer=answer+s[i]
        elif i%2==0:
            answer=answer+s[i].upper()
        else:
            answer=answer+s[i].lower()
    return answer
answer=""
check=0
s="try hello world"
for i in range(len(s)):
    if s[i]==" ":
        check=0
        answer=answer+s[i]
    elif check%2==0:
        answer=answer+s[i].upper()
        check=check+1
    else:
        answer=answer+s[i]
        check=check+1
    print(i,check)
print(answer)