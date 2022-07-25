from itertools import combinations   

def solution(nums):
    def prime(m):
        for l in range(2,m):
            if m % l==0:
                return False
            
        return True
    answer=0
    n=list(combinations(nums, 3))
    d=len(n)
    m=0
    for i in range(d):
        m=sum(n[i])
    
        if prime(m)==True:
            answer=answer+1
    return answer     



