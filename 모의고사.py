def solution(answers):
    answers_len=len(answers)
    one=[]
    two=[]
    answer=[]
    three=[]
    one_c=0
    two_c=0
    three_c=0
    l=0
    o=1
    j=0 #12345
    t=[2,1,2,3,2,4,2,5] #2123242521232425
    th=[3,3,1,1,2,2,4,4,5,5] #3311224455 3311224455
    for i in range(answers_len):
        if l>len(t)-1:
            l=0
        if o>5:
            o=1
        one.append(o)
        o=o+1
        two.append(t[l])
        l=l+1    
        if j>len(th)-1:
            j=0
        three.append(th[j])
        j=j+1
    for d in range(answers_len):
        if one[d]==answers[d]:
            one_c=one_c+1
        if two[d]==answers[d]:
            two_c=two_c+1
        if three[d]==answers[d]:
            three_c=three_c+1

    if max(one_c,two_c,three_c)==one_c:
        answer.append(1)
    if max(one_c,two_c,three_c)==two_c:
        answer.appned(2)    
    if max(one_c,two_c,three_c)==three_c:
        answer.appned(3)

    return answer
# answers=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
# answers_len=len(answers)
# one=[]
# two=[]
# answer=[]
# three=[]
# one_c=0
# two_c=0
# three_c=0
# l=0
# o=1
# j=0 #12345
# t=[2,1,2,3,2,4,2,5] #2123242521232425
# th=[3,3,1,1,2,2,4,4,5,5] #3311224455 3311224455
# for i in range(answers_len):
#     if l>len(t)-1:
#         l=0
#     if o>5:
#         o=1
#     one.append(o)
#     o=o+1
#     two.append(t[l])
#     l=l+1    
#     if j>len(th)-1:
#         j=0
#     three.append(th[j])
#     j=j+1
# for d in range(answers_len):
#     if one[d]==answers[d]:
#         one_c=one_c+1
#     if two[d]==answers[d]:
#         two_c=two_c+1
#     if three[d]==answers[d]:
#         three_c=three_c+1

# if max(one_c,two_c,three_c)==one_c:
#     answer.append(1)
# if max(one_c,two_c,three_c)==two_c:
#     answer.appned(2)    
# if max(one_c,two_c,three_c)==three_c:
#     answer.appned(3)


