def solution(board, moves):

    basket=[0,1,0]
    answer=0
    d=len(board)
    for i in moves:
        for l in range(d):
            if board[:][l][i-1] != 0: 
            
                basket.append(board[:][l][i-1])
                board[:][l][i-1]=0
                if basket[-1]==basket[-2]:
                    answer=answer+2
                    del basket[-2:]
                break
    return answer