def solution(s):
    p_count=0
    y_count=0
    for i in range(len(s)):
        if s[i]=='p' or s[i]=='P':
            p_count=p_count+1
        if s[i]=='y' or s[i]=='Y':
            y_count=y_count+1
    if p_count==y_count:
        return True
    else:
        return False
s="Pyy"
p_count=0
y_count=0
for i in range(len(s)):
    print(s[i])
    if s[i]=='p' or s[i]=='P':
        p_count=p_count+1
    elif s[i]=='y' or s[i]=='Y':
        y_count=y_count+1
print(p_count)
print(y_count)
if p_count==y_count:
    print("t")
else:
    print("f")