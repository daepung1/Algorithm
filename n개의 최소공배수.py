"""
두 수의 최소공배수(Least Common Multiple)란 
입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
예를 들어 2와 7의 최소공배수는 14가 됩니다.
 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다.
  n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.
  n개의 수를 곱한 후 n개의 최대공약수로 나눠
"""
def solution(arr):
    
    arr=sorted(arr,reverse=True)
    while(True):
        if len(arr)==1:
            break
        arr0_list=[]
        arr1_list=[]
        mix=[]
        print(arr)
        temp1=0
        temp2=0
        for i in range(1,arr[-1]+1):
            if arr[-1]%i==0:
                arr0_list.append(i)
        for i in range(1,arr[-2]+1):
            if arr[-2]%i==0:
                arr1_list.append(i)
        for i in range(len(arr0_list)):
            for l in range(len(arr1_list)):
                if arr0_list[i]==arr1_list[l]:
                    mix.append(arr0_list[i])
        temp1=arr[-1]
        temp2=arr[-2]
        arr.pop()
        arr.pop()
        arr.append(int(temp1*temp2/max(mix)))
        
    return arr[0]
arr=[2,6,8,14]

arr=sorted(arr,reverse=True)
while(True):
    if len(arr)==1:
        break
    arr0_list=[]
    arr1_list=[]
    mix=[]
    print(arr)
    temp1=0
    temp2=0
    for i in range(1,arr[-1]+1):
        if arr[-1]%i==0:
            arr0_list.append(i)
    for i in range(1,arr[-2]+1):
        if arr[-2]%i==0:
            arr1_list.append(i)
    for i in range(len(arr0_list)):
        for l in range(len(arr1_list)):
            if arr0_list[i]==arr1_list[l]:
                mix.append(arr0_list[i])
    temp1=arr[-1]
    temp2=arr[-2]
    arr.pop()
    arr.pop()
    arr.append(int(temp1*temp2/max(mix)))
    print(arr)
print(arr)