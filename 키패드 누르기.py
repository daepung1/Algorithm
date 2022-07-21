"""
 1   2   3                
 4   5   6
 7   8   9
10  11 12
leftcen으로 나올 수 있는 값
왼손이 1이라 가정
1,4,7,10
왼손이 4 라 가정
2,1,4,7
왼손이 7이라 가정
1,2,



rightcen으로 나올 수 있는 값
"""
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
            if lefthand==1:
                if i==2:
                    leftcen=1
                elif i==5:
                    leftcen=2
                elif i==8:
                    leftcen=3
                elif i==11:
                    leftcen=4
            elif lefthand==2:
                if i==2:
                    leftcen=0
                elif i==5:
                    leftcen=1
                elif i==8:
                    leftcen=2
                elif i==11:
                    leftcen=3
            elif lefthand==4:
                if i==2:
                    leftcen=2
                elif i==5:
                    leftcen=1
                elif i==8:
                    leftcen=2
                elif i==11:
                    leftcen=3
            elif lefthand==5:
                if i==2:
                    leftcen=1
                elif i==5:
                    leftcen=0
                elif i==8:
                    leftcen=1
                elif i==11:
                    leftcen=2
            elif lefthand==7:
                if i==2:
                    leftcen=3
                elif i==5:
                    leftcen=2
                elif i==8:
                    leftcen=1
                elif i==11:
                    leftcen=2
            elif lefthand==8:
                if i==2:
                    leftcen=2
                elif i==5:
                    leftcen=1
                elif i==8:
                    leftcen=0
                elif i==11:
                    leftcen=0
            elif lefthand==10:
                if i==2:
                    leftcen=4
                elif i==5:
                    leftcen=3
                elif i==8:
                    leftcen=2
                elif i==11:
                    leftcen=1
            elif lefthand==11:
                if i==2:
                    leftcen=3
                elif i==5:
                    leftcen=2
                elif i==8:
                    leftcen=1
                elif i==11:
                    leftcen=0
            if righthand==3:
                if i==2:
                    rightcen=1
                elif i==5:
                    rightcen=2
                elif i==8:
                    rightcen=3
                elif i==11:
                    rightcen=4
            elif righthand==2:
                if i==2:
                    rightcen=0
                elif i==5:
                    rightcen=1
                elif i==8:
                    rightcen=2
                elif i==11:
                    rightcen=3
            elif righthand==6:
                if i==2:
                    rightcen=2
                elif i==5:
                    rightcen=1
                elif i==8:
                    rightcen=2
                elif i==11:
                    rightcen=3
            elif righthand==5:
                if i==2:
                    rightcen=1
                elif i==5:
                    rightcen=0
                elif i==8:
                    rightcen=1
                elif i==11:
                    rightcen=2
            elif righthand==9:
                if i==2:
                    rightcen=3
                elif i==5:
                    rightcen=2
                elif i==8:
                    rightcen=1
                elif i==11:
                    rightcen=2
            elif righthand==8:
                if i==2:
                    rightcen=2
                elif i==5:
                    rightcen=1
                elif i==8:
                    rightcen=0
                elif i==11:
                    rightcen=0
            elif righthand==12:
                if i==2:
                    rightcen=4
                elif i==5:
                    rightcen=3
                elif i==8:
                    rightcen=2
                elif i==11:
                    rightcen=1
            elif righthand==11:
                if i==2:
                    rightcen=3
                elif i==5:
                    rightcen=2
                elif i==8:
                    rightcen=1
                elif i==11:
                    rightcen=0
            if rightcen>leftcen:
                lefthand=i
                click="L"
                answer=answer+click
            elif leftcen>rightcen:
                righthand=i
                click="R"
                answer=answer+click
            else:
                if hand=="left":
                    lefthand=i
                    click="L"
                    answer=answer+click
                else:
                    righthand=i
                    click="R"
                    answer=answer+click
    return answer
