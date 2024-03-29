"""
△△ 게임대회가 개최되었습니다. 이 대회는 N명이 참가하고, 토너먼트 형식으로 진행됩니다.
 N명의 참가자는 각각 1부터 N번을 차례대로 배정받습니다.
  그리고, 1번↔2번, 3번↔4번, ... , N-1번↔N번의 참가자끼리 게임을 진행합니다. 
  각 게임에서 이긴 사람은 다음 라운드에 진출할 수 있습니다. 
  이때, 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받습니다. 
  만약 1번↔2번 끼리 겨루는 게임에서 2번이 승리했다면 다음 라운드에서 1번을 부여받고, 3번↔4번에서 겨루는 게임에서 
  3번이 승리했다면 다음 라운드에서 2번을 부여받게 됩니다. 게임은 최종 한 명이 남을 때까지 진행됩니다.

이때, 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 궁금해졌습니다.
게임 참가자 수 N, 참가자 번호 A, 경쟁자 번호 B가 함수 solution의 매개변수로 주어질 때,
 처음 라운드에서 A번을 가진 참가자는 경쟁자로 생각하는 B번 참가자와 몇 번째 라운드에서 만나는지 return 하는 solution 함수를 완성해 주세요.
  단, A번 참가자와 B번 참가자는 서로 붙게 되기 전까지 항상 이긴다고 가정합니다.

제한사항
N : 21 이상 220 이하인 자연수 (2의 지수 승으로 주어지므로 부전승은 발생하지 않습니다.)
A, B : N 이하인 자연수 (단, A ≠ B 입니다.)
입출력 예
N	A	B	answer
8	4	7	3

"""


def solution(n,a,b):
    temp=[]
    t=0
    answer=1
    
    for i in range(n):
        temp.append(i+1)
    
    count=0
    a=a-1
    b=b-1
    while(True):
        if abs(temp[a]-temp[b])==1:
            break
        for i in range(len(temp)):
            temp[i]=temp[i]-t
            if count==0:
                t=t+1
                count=1
            else:
                t=t
                count=0
        answer=answer+1
        t=0
        temp=list(set(temp))
        
        a=a//2
        b=b//2
    return answer
# 1 12  2 34 3 56 4 78 5 910 
#   01    12   23   34   45
temp=[]
t=0
f=1
n=8
for i in range(n):
    temp.append(i+1)
a=4
b=5
count=0
answer=1
a=a-1
b=b-1

while(True):
    c=max(a,b)
    if c%2==0:
        c=c
    elif abs(temp[a]-temp[b])==1:
        break
    for i in range(len(temp)):
        temp[i]=temp[i]-t
        if count==0:
            t=t+1
            count=1
        else:
            t=t
            count=0
    answer=answer+1
    t=0
    temp=list(set(temp))
    
    a=a//2
    b=b//2
print(answer)
# 1 12  2 34 3 56 4 78 5 910 
#   01    12   23   34   45
# 0 01 1 23 2 45 3 67
#   12   34   56   78 
#        a-1      b-1
#         3        6
#  1  2   3    4
# 0   1   2    3