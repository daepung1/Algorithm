a, b = map(int, input().strip().split(' '))
temp=""
for i in range(a):
    temp=""
    for l in range(b):
        temp=temp+"*"
    print(temp)