def solution(arr):
    
    arr.remove(min(arr))
    if len(arr)==0:
        arr=[-1]
    return arr

answer=[1,23,4]

answer.remove(min(answer))
if len(answer)==0:
    answer=-1