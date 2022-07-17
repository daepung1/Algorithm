import re
def solution(new_id):
    new_id=new_id.lower()#1단계
    text=re.sub('[^0-9a-z-_.]','',new_id)#2단계 # re.sub('[필터링,'뭐로바꿀지',문자열])
    new_id=text
    while(True):
        new_id=re.sub('[.]{2}','.',new_id) #3단계
        if len(re.findall('[.]{2}',new_id))==0:
            break   
    try:
        if new_id.strip()[-1] == '.': #4단계
            new_id=new_id[:-1]
        if new_id.strip()[0]=='.':
            new_id=new_id[1:]
        print(new_id)
    except:
        print("예외발생")
    new_id_len=len(new_id)
    
    if new_id_len==0:  #5단계
        new_id="a"
    if new_id_len>=16: #6단계
        new_id=new_id[0:15]
        if new_id.strip()[-1] == '.': 
            new_id=new_id[:-1]
    if new_id_len<=2: #7단계
        l=new_id[-1]
        while(new_id_len!=3):
            new_id=new_id+l
            new_id_len=len(new_id)

    answer = new_id
    return answer
