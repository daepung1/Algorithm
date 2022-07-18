def solution(s):
    ten_dict={
    "zero" : '0',
    "one" : '1',
    "two" : '2',
    "three" : '3',
    "four" : '4',
    "five" : '5',
    "six" : '6',
    "seven" : '7',
    "eight" : '8',
    "nine" : '9'
    }
    for num in ten_dict.keys():
        if num in s:
            s=s.replace(num,ten_dict[num])
    answer = int(s)
    return answer



