"""
https://bomoto.tistory.com/14
해당 글에서 힌트를 얻어 풀이하였음 내가 떠올린 방법은 아니지만 이해는 하였음
"""
import collections
def solution(N, stages):
    answer={}
    all_user=len(stages) # 1스테이지 도달한 유저 수
    a=collections.Counter(stages)
    dodal={}
    total=0

    for i in range(N):
        if i==0:
            i=i
        else:
            total=total+a[i]
        dodal[i+1]=all_user-total
        
    for i in range(N):
        if dodal[i+1]==0:
            answer[i+1]=0
        else:
            answer[i+1]=a[i+1]/dodal[i+1]
    answer=sorted(answer,key=lambda x : answer[1],reverse=True)
    

    return answer

#실패율 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
N=4
answer={}
stages=[4,4,4,4,4]
all_user=len(stages) # 1스테이지 도달한 유저 수
a=collections.Counter(stages)
dodal={}
total=0

for i in range(N):
    if i==0:
        i=i
    else:
        total=total+a[i]
    dodal[i+1]=all_user-total
    
for i in range(N):
    answer[i+1]=a[i+1]/dodal[i+1]
ans=[]
answer=sorted(answer,key=lambda x : answer[1],reverse=True)
print(answer)

