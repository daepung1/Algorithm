import collections
def solution(participant, completion):
    answer = ''
    artcount=collections.Counter(participant)
    
    comcount=collections.Counter(completion)
    d=artcount-comcount
    ans=d.keys()
    for i in ans:
        answer=i
    return answer

# articipant=["mislav", "stanko", "ana","mislav","stanko"]
# completion=["stanko", "ana", "mislav"]
# artcount=collections.Counter(articipant)
# print(artcount)
# comcount=collections.Counter(completion)
# print(comcount)
# print(artcount-comcount)
# d=artcount-comcount
# ans=d.keys()
# for i in ans:
#     answer=i