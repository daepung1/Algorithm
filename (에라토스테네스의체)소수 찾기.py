def solution(n):
    if n==2:
        answer=1
    elif n==3:
        answer=3
    else:
        answer=2
        for i in range(4,n+1):
            for l in range(2,n):
                if i<=l:
                    break
                if i%l !=0:
                    if l==i-1:
                        answer=answer+1
                    else:
                        l=l
                else:
                    break
        
    
    return answer
# n=20
# a = [False,False] + [True]*(n-1)
# count=0
# print(a)
# for i in range(2,n+1):
#     if a[i]:
#         count=count+1
#         print("a",a)
#         print("i",i)

#         for j in range(2*i, n+1, i):
#             a[j] = False
#             print("j",j)
# print(a)
def solution(n):

    a = [False,False] + [True]*(n-1)
    answer=0
    for i in range(2,n+1):
        if a[i]:
            answer=answer+1
            for j in range(2*i, n+1, i):
                a[j] = False
    
    return answer
#에라토스테네스의 체
n=20

ans=[0,0]
count=0
for i in range(2,n+1):
    ans.append(i)
print(ans)
for i in range(2,n+1):
    if ans[i]!=0:
        count=count+1
    for l in range(2*i,n+1,i):
        ans[l]=0
        print(l)
print(ans)
print(count)        