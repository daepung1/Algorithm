def solution(s, n):
    answer=""
    alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    big_alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alpha_check=alpha+big_alpha
    for i in range(len(s)):
        if s[i] not in alpha_check:
            answer=answer+s[i]
        else:
            for l in range(len(alpha)):
                if s[i]==alpha[l]:
                    check=l+n
                    if check>len(alpha)-1:
                        check=check-len(alpha)
                    answer=answer+alpha[check]
                    break
                elif s[i]==big_alpha[l]:
                    check=l+n
                    if check>len(alpha)-1:
                        check=check-len(alpha)
                    answer=answer+big_alpha[check]
                    break
        
            check=0
    return answer
n=1
s="z B"
check=0
answer=""
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_check=alpha+big_alpha
for i in range(len(s)):
    if s[i] not in alpha_check:
        answer=answer+s[i]
    else:
        for l in range(len(alpha)):
            if s[i]==alpha[l]:
                check=l+n
                if check>len(alpha)-1:
                    check=check-len(alpha)
                answer=answer+alpha[check]
                break
            elif s[i]==big_alpha[l]:
                check=l+n
                if check>len(alpha)-1:
                    check=check-len(alpha)
                answer=answer+big_alpha[check]
                break
    
        check=0
    print(answer)
