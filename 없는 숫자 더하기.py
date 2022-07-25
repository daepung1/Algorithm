def solution(numbers):
    full_number=[1,2,3,4,5,6,7,8,9]

    answer=0
    add_list=[i for i in full_number if i not in numbers]
    for l in add_list:
        answer=answer+l
    return answer

