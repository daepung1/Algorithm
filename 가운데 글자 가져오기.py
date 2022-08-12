def solution(s):
    answer = ''
    len_s=len(s)

    if len_s/2 ==len_s//2:
        answer=s[len_s//2-1]+s[(len_s//2)]
        
    else:
        answer=s[len_s//2]
    return answer

s="qwer"

len_s=len(s)

if len_s/2 ==len_s//2:
    print("a")
    print(s[len_s//2-1]+s[(len_s//2)])
    
else:
    print(s[len_s//2])