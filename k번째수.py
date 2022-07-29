def solution(array, commands):
    def k_number(array,k):
        k_len=len(k)
        ans=[]
        dept=[]
        for i in range(k_len):
            d=0
            l=1
            j=2
            dept=array[(k[i][d]-1):k[i][l]]
            dept=sorted(dept)
            a=k[i][j]-1
            ans.append(dept[a])
        return ans
        
    answer = k_number(array,commands) 
    return answer
# def k_number(array,k):
#     k_len=len(k)
#     ans=[]
#     dept=[]
#     for i in range(k_len):
#         d=0
#         l=1
#         j=2
#         print(k[i][i],":",k[i][l])
#         dept=array[(k[i][d]-1):k[i][l]]
#         dept=sorted(dept)
#         print(dept)
#         a=k[i][j]-1
#         print(dept[a])
#         ans.append(dept[a])
#     return ans


# array=[1, 5, 2, 6, 3, 7, 4]
# k=[[2,5,3],[4,4,1],[1,7,3]]
# print(k_number(array,k))
