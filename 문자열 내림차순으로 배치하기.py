def solution(s):
    answer=""
    s = sorted(s,reverse=True)
    for i in s:
        answer=answer+i
    return answer
s="Zbcdefg"

s=sorted(s,reverse=True)

print(s)