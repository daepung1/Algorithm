def solution(n):
        
    for i in range(1,1000000):
        if n%i==1:
        
            return i
        else:
            return n

n=0
for i in range(2,50000):
    if n%i==1:
        print(i)
# 문제에서 범위를 3~1000000이라고 줘서 그냥 10000000을
# 넣었는대 생각해보면 n을 넣는것이 더 합리적이다
