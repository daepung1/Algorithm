def solution(numbers, hand):
    left=[1,4,7,10] # 왼손으로 눌러야 하는 애들
    right=[3,6,9,12] # 오른손으로 눌러야 하는 애들
    center=[11,2,5,8] # 오른손인지 왼손인지 상황에 따라 다름
    lefthand=10 # * 왼손의 위치
    righthand=12 # # 오른손의 위치
    rcenter=0 # 왼손과 가운데 애들의 거리
    lcenter=0 # 오른손가 가운데 애들의 거리
    answer = ''
    click='' # 오른손으로 누를건지 왼손으로 누를건지
    for i in numbers:
        if i==0:
            i=11
        if i in left:
            click="L"
            answer=answer+click
            lefthand=i
        elif i in right:
            click="R"
            answer=answer+click
            righthand=i
        elif i in center:
            rcenter=abs(righthand-i)
            lcenter=abs(lefthand-i)
            if righthand in center:
                if abs(righthand-i)==3:
                    rcenter=1
                elif abs(righthand-i)==6:
                    rcenter=2
                elif abs(righthand-i)==9:
                    rcenter=3
            if lefthand in center:
                if abs(lefthand-i)==3:
                    lcenter=1
                elif abs(lefthand-i)==6:
                    lcenter=2
                elif abs(lefthand-i)==9:
                    lcenter=3
            if rcenter==2 and lcenter==4:  #2 차 보안
                rcenter=0# 같은 거리 만들어주기
                lcenter=0# 같은 거리 만들어주기
            if rcenter==4 and lcenter==2:
                rcenter=0
                lcenter=0        
            if rcenter>lcenter:
                click="L"
                answer=answer+click
                lefthand=i
            elif rcenter<lcenter:
                click="R"
                answer=answer+click
                righthand=i
            else:
                if hand=='left':
                    lefthand=i
                    click="L"
                    answer=answer+click
                else:
                    righthand=i
                    click="R"
                    answer=answer+click
    return answer
