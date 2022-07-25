def solution(absolutes, signs):
    answer=0

    d=len(absolutes)

    for i in range(d):
        if signs[i]==False:
            absolutes[i]=-absolutes[i]
        answer=answer+absolutes[i]
    
    return answer