def solution(board, moves):

    basket=[]
    t=0
    answer=0
    for i in moves:
        if i==1:
            t=board[0].pop()
            if t==0:
                print("잡을 것이 없습니다")
            else:
                basket.append(t)
        elif i==2:
            t=board[1].pop()
            if t==0:
                print("잡을 것이 없습니다")
            else:
                basket.append(t)
        elif i==3:
            t=board[2].pop()
            if t==0:
                print("잡을 것이 없습니다")
            else:
                basket.append(t)
                
        elif i==4:
            t=board[3].pop()
            if t==0:
                print("잡을 것이 없습니다")
            else:
                basket.append(t)
        elif i==5:
            t=board[4].pop()
            if t==0:
                print("잡을 것이 없습니다")
            else:
                basket.append(t)
               
    return answer