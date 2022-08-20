def solution(strings, n):
    strings=sorted(strings)
    
    strings=sorted(strings,key=lambda x :x[n])
    return strings
#이렇게 쉬운걸 한참 돌아갓다
# def solution(strings, n):
#     temp=[]
#     tempstr=""
#     p=0
#     for i in range(len(strings)):
#         if strings[i][n]==tempstr:
#             temp.append(tempstr)
#         tempstr=strings[i][n]
#     temp=set(temp)       

#     temp2=[i for i in strings if i[n] in temp]

#     temp2=sorted(temp2)
#     temp3=[i for i in strings if i[n] not in temp]

#     answer=temp2+temp3
#     answer=sorted(answer,key=lambda x : x[n])

#     return answer

strings=["zbcde", "ybcdf", "xbcdg","dd","aa","aa" ]
n=1
strings=sorted(strings)
strings=sorted(strings,key=lambda x :x[n])
print(strings)