s="(())()"
def solution(s):
    a=["a"]
    for i in range(len(s)):
        if s[i]=="(":
            a.append("1")
        else:
            a.pop()
    if a[-1]=="a":
        return True
    else:
        False