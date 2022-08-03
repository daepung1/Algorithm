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
    stages_count=collections.Counter(stages)
    stages_count=dict(collections.OrderedDict(sorted(stages_count.items())))
    stages_clear={}
    for i in stages:
        counter=0
        for l in stages:
            if i<=l:
                counter=counter+1
        stages_clear[i]=counter
    stages_clear=dict(sorted(stages_clear.items()))
    temp=[]
    temp2=[]
    for i in range(N):
        temp.append(i+1)
    temp_key=[]
    temp_values=[]
    temp_key2=[]
    temp_values2=[]

    i=0
    if N!=len(stages_count):
        
        for i,l in stages_count.items():
            if i>N:
                i=i
            else:
                temp_key.append(i)
                temp_values.append(l)
        for i,l in stages_clear.items():
            if i>N:
                i=i
            else:
                temp_key2.append(i)
                temp_values2.append(l)
        
        for i in range(len(temp_key)):
            answer_1[(temp_key[i])]=temp_values[i]/temp_values2[i]
        answer_1=sorted(answer_1, key= lambda x : answer_1[x],reverse=True)
        temp2=[i for i in temp if i not in answer_1]

        answer=answer_1+temp2
        
        
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
N=4
stages=[4,4,4,3,3,5]        
stages_count=collections.Counter(stages)
stages_count=dict(collections.OrderedDict(sorted(stages_count.items())))
stages_clear={}
for i in stages:
    counter=0
    for l in stages:
        if i<=l:
            counter=counter+1
    stages_clear[i]=counter
stages_clear=dict(sorted(stages_clear.items()))
temp=[]
temp2=[]
for i in range(N):
    temp.append(i+1)
temp_key=[]
temp_values=[]
temp_key2=[]
temp_values2=[]

i=0
if N!=len(stages_count):
    
    for i,l in stages_count.items():
        if i>N:
            i=i
        else:
            temp_key.append(i)
            temp_values.append(l)
    for i,l in stages_clear.items():
        if i>N:
            i=i
        else:
            temp_key2.append(i)
            temp_values2.append(l)
    
    for i in range(len(temp_key)):
        answer_1[(temp_key[i])]=temp_values[i]/temp_values2[i]
    answer_1=sorted(answer_1, key= lambda x : answer_1[x],reverse=True)
    temp2=[i for i in temp if i not in answer_1]

    answer=answer_1+temp2
    print(answer)
    
else:
    for i in range(len(stages_clear)):

        try:
            answer_1[i+1]=stages_count[i+1]/stages_clear[i+1]
        except:
            answer_1[i+1]=N/20000

        answer= sorted(answer_1, key= lambda x : answer_1[x],reverse=True)
        print(answer)