"""
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
"""
def solution(arr1, arr2):
    answer=[]
    for i in range(len(arr1)):
        ans={}
        for l in range(len(arr1[0])):
            for j in range(len(arr2[0])):
                if j in ans.keys():
                    ans[j]=ans[j]+arr1[i][l]*arr2[l][j]
                        
                else:
                    ans[j]=arr1[i][l]*arr2[l][j]
        answer.append(list(ans.values()))

    return answer

arr1=[[1,2,3,4], [1,2,3,4]]
arr2=[[1,2], [1,2], [1,2], [1,2]]
answer=[]
temp=arr1


for i in range(len(arr1)):
    ans={}
    for l in range(len(arr1[0])):
        for j in range(len(arr2[0])):
            if j in ans.keys():
                ans[j]=ans[j]+arr1[i][l]*arr2[l][j]
                
                    
            else:
                ans[j]=arr1[i][l]*arr2[l][j]
            print(answer)
    answer.append(list(ans.values()))
    print(answer)
        
       
