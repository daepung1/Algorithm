from itertools import product
def solution(sizes):
    w=[]
    h=[]
    for i in range(len(sizes)):
        if sizes[i][0]>=sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            w.append(sizes[i][1])
            h.append(sizes[i][0])
    return max(w)*max(h)


answer=[]
w=[]
h=[]
count=0
reverse=[]
sizes=[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
#reverse=[[4, 14], [6, 19], [16, 6], [7, 18], [11, 7]]
for i in range(len(sizes)):
    if sizes[i][0]>=sizes[i][1]:
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    else:
        w.append(sizes[i][1])
        h.append(sizes[i][0])
print(max(w))
print(max(h))
"""
from itertools import product
def solution(sizes):
    answer=[]
    w=[]
    h=[]
    count=0

    for i in range(len(sizes)):
        w.append(sizes[i][0])
        h.append(sizes[i][1])
    w=sorted(w)
    h=sorted(h)
    if w[-1]>=h[-1]:
        sizes_max=[w[-1]]
        check=0 #w 가 젤 큰값일때
    else:
        sizes_max=[h[-1]]
        check=1 # h가 젤 큰값일때

    if check==0:
        whpro=list(product(sizes_max,h))
    else:
        whpro=list(product(w,sizes_max))
    for i in range(len(whpro)):
        count=0
        if whpro[i][0]>whpro[i][1]:
            big=whpro[i][0]
            small=whpro[i][1]
        else:
            big=whpro[i][1]
            small=whpro[i][0]
        for l in range(len(sizes)):
            if sizes[l][0]>sizes[l][1]:
                big1=sizes[l][0]
                small1=sizes[l][1]
            else:
                big1=sizes[l][1]
                small1=sizes[l][0]
            if big>=big1 and small>=small1:
                count=count+1
            else:
                break
        if count==len(sizes):
            answer.append(whpro[i][0]*whpro[i][1])
    return min(answer)
"""