def solution(s):
    s_int=[1,2,3,4,5,6,7,8,9,0]
    count=0
    if len(s)==4 or len(s)==6:
        count=count+1
    for i in s:
        if i in s_int:
            i=i
        else:
            return False
    if count==1:
        return True
    else:
        return False
s="1234"
print(len(s))
s_int=[1,2,3,4,5,6,7,8,9,0]
count=0
if len(s)==4 or len(s)==6:
    count=count+1
for i in s:
    if i in s_int:
        i=i
    else:
        print("f")
if count==1:
    print("t")
else:
    print("f") 