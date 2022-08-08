from itertools import combinations


def solution(numbers):
    answer = []
    return answer
numbers=[2,1,3,4,1]
answer=[]
d=list(combinations(numbers,2))
for i in range(len(d)):
    answer.append(d[i][0]+d[i][1])
answer=list(set(answer))
print(answer)