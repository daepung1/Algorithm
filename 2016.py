def solution(a, b):
    answer=''
    c=0
    day=['SUN','MON','TUE','WED','THU','FRI','SAT']
    month={1:0,
    2:31,
    3:60,
    4:91,
    5:121,
    6:152,
    7:182,
    8:213,
    9:244,
    10:274,
    11:305,
    12:335}

    c=month[a]+b
    if c%7==0:
        answer=day[4]
    elif c%7==1:
        answer=day[5]
    elif c%7==2:
        answer=day[6]
    elif c%7==3:
        answer=day[0]
    elif c%7==4:
        answer=day[1]
    elif c%7==5:
        answer=day[2]
    else:
        answer=day[3]
    return answer

a=6
b=6
c=0
day=['SUN','MON','TUE','WED','THU','FRI','SAT']
month={2:31,
3:60,
4:91,
5:121,
6:152,
7:182,
8:213,
9:244,
10:274,
11:305,
12:335}

c=month[a]+b
if c%7==0:
    answer=day[4]
elif c%7==1:
    answer=day[5]
elif c%7==2:
    answer=day[6]
elif c%7==3:
    answer=day[0]
elif c%7==4:
    answer=day[1]
elif c%7==5:
    answer=day[2]
else:
    answer=day[3]
print(answer)