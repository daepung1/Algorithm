import sys
sys.setrecursionlimit(10**7)
"""
효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)
의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다.
 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 
 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수,
solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.
"""
def solution(n):
    
    def fac1(n,d):
        answer=1
        for i in range(d):
            answer=answer*(n-i)
        return answer
    def fac(n):
        if n==1:
            return 1
        return n*fac(n-1)
    one_count=0
    arr=[]
    answer=1
    for i in range(n):
        arr.append(1)
    for i in range(len(arr)):
        if arr[i]==1:
            one_count=one_count+1
        if one_count==2:
            arr[i]=0
            arr[i-1]=0
            one_count=0
            if arr.count(1)==0:
                answer=answer+1
                break
            answer=answer+fac1(arr.count(1)+(arr.count(0)//2),arr.count(1))//fac(arr.count(1))
                    
    return answer%1234567
def fac1(n,d):
    answer=1
    for i in range(d):
        answer=answer*(n-i)
    return answer
def fac(n):
    if n==1:
        return 1
    return n*fac(n-1)
one_count=0
n=2000
arr=[]
answer=1
for i in range(n):
    arr.append(1)
for i in range(len(arr)):
    if arr[i]==1:
        one_count=one_count+1
    if one_count==2:
        arr[i]=0
        arr[i-1]=0
        one_count=0
        if arr.count(1)==0:
            answer=answer+1
            break
        # print(fac1(len(arr),arr.count(1)))  
        # print(fac(arr.count(1))) 
        print("d",fac1((arr.count(0)//2)+arr.count(1),arr.count(1))//fac(arr.count(1)))
        answer=answer+fac1(arr.count(1)+(arr.count(0)//2),arr.count(1))//fac(arr.count(1))
        # print(arr)
        # print(arr.count(0)//2) # 2의개수
        # print(arr.count(1)) #1의 개수
        # print(len(arr)) # len(arr)c 1
        # if arr.count(0)//2==1 or arr.count(1)
# print(fac1(6,4))  
# print(fac(4)) 
# print(fac1(5,1)/fac(1))    
print(answer)