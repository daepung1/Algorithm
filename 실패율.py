"""
import collections

d = {2:13, 1:9, 4:25, 3:0}
collections.Counter() 
result = collections.OrderedDict(sorted(d.items())) 얘내들을 사용하여 쉽게 풀이
d=sorted(d.items(),key=lambda x: x[1], reverse=True) 람다식을 사용하여 딕셔너리를 밸류기준으로 정렬
람다식 공부좀 해보자
"""
import collections
def solution(N, stages): 
    
    answer_1={}
    answer=[]
    stages_len=len(stages) 
    stages_count=collections.Counter(stages)
    stages_count=dict(collections.OrderedDict(sorted(stages_count.items())))
    stages_stack=0
    stages_clear={}
    for i in stages_count:
        if stages_len-stages_count[i]==0:
            stages_clear[i]=-1
        else:
            try:
                stages_stack=stages_stack+stages_count[i-1]    
                stages_clear[i]=stages_len-stages_stack
            except:
                stages_clear[i]=stages_len
    stages_clear=dict(sorted(stages_clear.items()))
    temp=[]
    temp2=[]

    # if N+1 in list(stages_count.keys()):
    #     stages_count.pop(N+1)
    #     stages_clear.pop(N+1)
        

    i=0
    if N!=len(stages_count):
        for i in range(N):
            temp.append(i+1)
        for k in stages_count.keys():
            if k > N:
                k=k
            else: 
                if k in stages_clear.keys():
                
                    answer_1[k]=stages_count[k]/stages_clear[k]
        
                
        answer_1=sorted(answer_1,key=lambda x: answer_1[x], reverse=True)
        
        temp2=[i for i in temp if i not in answer_1]

        answer=answer_1+temp2
        return answer
        
    else:
        for i in range(len(stages_clear)):

            try:
                answer_1[i+1]=stages_count[i+1]/stages_clear[i+1]
            except:
                answer_1[i+1]=N/20000

        answer= sorted(answer_1, key= lambda x : answer_1[x],reverse=True)
        return answer    

#----------------------------------------------------------------------





answer_1={}
answer=[]
# N=5
# stages=[2, 1, 2, 6, 2, 4, 3, 3]
N=8
stages=[1,2,3,4,5,6,7]        
stages_len=len(stages)
stages_count=collections.Counter(stages)
stages_count=dict(collections.OrderedDict(sorted(stages_count.items())))
print(stages_count)
stages_stack=0
stages_clear={}
for i in stages_count:
    if stages_len-stages_count[i]==0:
        stages_clear[i]=-1
    else:
        try:
            stages_stack=stages_stack+stages_count[i-1]    
            stages_clear[i]=stages_len-stages_stack
        except:
            stages_clear[i]=stages_len
stages_clear=dict(sorted(stages_clear.items()))
print(stages_clear)
print(stages_count)
temp=[]
temp2=[]

# if N+1 in list(stages_count.keys()):
#     stages_count.pop(N+1)
#     stages_clear.pop(N+1)
    

i=0
if N!=len(stages_count):
    for i in range(N):
            temp.append(i+1)
        
    for k in stages_count.keys():
        if k > N or k<1:
            k=k
           
        else: 
            if k in stages_clear.keys():
            
                answer_1[k]=stages_count[k]/stages_clear[k]
    
    answer_1=sorted(answer_1,key=lambda x: answer_1[x], reverse=True)
    
    temp2=[i for i in temp if i not in answer_1]
    if temp2[-1]>=N:
        temp2.pop()
    
    answer=answer_1+temp2
    print(answer)
    print("1")
else:
    
    for i in range(len(stages_clear)):

        try:
            answer_1[i+1]=stages_count[i+1]/stages_clear[i+1]
        except:
            answer_1[i+1]=N/20000
    print("2")
    answer= sorted(answer_1, key= lambda x : answer_1[x],reverse=True)
    print(answer)