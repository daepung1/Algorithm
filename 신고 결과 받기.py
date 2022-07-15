import collections
def solution(id_list, report, k):
    report=set(report)
    report=list(report)
    report_len=len(report)
    answer=[] 
    ad=[] #신고자
    ab=[] #신고당한사람
    ab_count={}
    ad2=[] #최종 k번 이상 신고자들 모음
    ab2=[] #ad2 신고자들 모음
    for rep in report:
        ad.append(rep.split(" ")[0])
        ab.append(rep.split(" ")[1])

    ab_count=collections.Counter(ab)

    for key, value in ab_count.items():
        if value >= k:   
            ad2.append(key)

    for rep2 in report:
        if rep2.split(" ")[1] in ad2:
            ab2.append(rep2.split(" ")[0])

    for id1 in id_list:
        count=0
        for check in ab2:
            if id1 == check:
                count=count+1
        answer.append(count)  

    return answer
