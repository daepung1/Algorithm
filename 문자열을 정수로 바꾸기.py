def solution(s):
    p=1
    if s[0]=="-":
        p=-1
        s=s.replace("-","")
    s=int(s)
    answer=p*s
    
    return answer
s="-1234"
p=1
if s[0]=="-":
    p=-1
    s=s.replace("-","")
s=int(s)
answer=p*s
print(answer)
