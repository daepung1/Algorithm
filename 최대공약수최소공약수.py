"""
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
"""
"""
최소공배수를 구하는 방법을 몰라서 해맷는대 두 수를 곱한 후 최대공약수로 나누어주면 그것이 최소공배수이다
"""



def solution(n, m):
    answer = []
    n_list=[]
    m_list=[]
    count=0
    mix=[]
    for i in range(1,n+1):
        if n%i==0:
            n_list.append(i)
    for i in range(1,m+1):
        if m%i==0:
            m_list.append(i)
    for i in range(len(n_list)):
        for l in range(len(m_list)):
            if n_list[i]==m_list[l]:
                mix.append(n_list[i])
                break

    answer.append(max(mix))            
    answer.append((n*m)//answer[0])
           
    return answer
answer=[]
n=3
m=12
n_list=[]
m_list=[]
count=0
mix=[]
for i in range(1,n+1):
    if n%i==0:
        n_list.append(i)
for i in range(1,m+1):
    if m%i==0:
        m_list.append(i)
for i in range(len(n_list)):
    for l in range(len(m_list)):
        if n_list[i]==m_list[l]:
            mix.append(n_list[i])
            break

answer.append(max(mix))            
answer.append((n*m)//answer[0])

print(answer)