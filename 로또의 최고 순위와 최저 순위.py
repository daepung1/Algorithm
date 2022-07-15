def solution(lottos, win_nums):
    count=0
    zero_count=lottos.count(0)
    max_count=0
    answer = []
    
    for anum in lottos:
        if anum in win_nums:
            count=count+1

    max_count=count+zero_count
    
    if max_count==2:
        answer.append(5)
    elif max_count==3:
        answer.append(4)
    elif max_count==4:
        answer.append(3)
    elif max_count==5:
        answer.append(2)
    elif max_count==6:
        answer.append(1)
    else:
        answer.append(6)

    if count==2:
        answer.append(5)
    elif count==3:
        answer.append(4)
    elif count==4:
        answer.append(3)
    elif count==5:
        answer.append(2)
    elif count==6:
        answer.append(1)
    else:
        answer.append(6)

    
        
    
    return answer