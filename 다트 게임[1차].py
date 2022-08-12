def solution(dartResult):
    dart_int=["0","1","2","3","4","5","6","7","8","9"]

    answer=0
    one=[dartResult[0]]
    two=[]
    three=[]
    count=0
    for i in range(1,len(dartResult)):
        if dartResult[i] in dart_int:
            if dartResult[i]=="0" and dartResult[i-1]=="1":
                count=count
            else:
                count=count+1
        if count==0:
            one.append(dartResult[i])
        elif count==1:
            two.append(dartResult[i])
        else:
            three.append(dartResult[i])
    one_num=0
    two_num=0
    three_num=0
    for i in range(len(one)):
        if one[i] in dart_int:
            if one[0]=="1" and one[i]=="0":
                    one_num=10
                
                    
            else:
                
                one_num=int(one[i])
                        
        elif one[i] =="S":
            one_num=one_num
        elif one[i] =="D":
            one_num=one_num*one_num
        elif one[i] =="T":
            one_num=one_num*one_num*one_num
        elif one[i] =="*":
            one_num=one_num*2
        elif one[i] =="#":
            one_num=one_num*-1
        
    for i in range(len(two)):
        if two[i] in dart_int:
            if two[0]=="1" and two[i]=="0":
                    two_num=10
                
                    
            else:
                
                two_num=int(two[i])
                        
        elif two[i] =="S":
            two_num=two_num
        elif two[i] =="D":
            two_num=two_num*two_num
        elif two[i] =="T":
            two_num=two_num*two_num*two_num
        elif two[i] =="*":
            one_num=one_num*2
            two_num=two_num*2
        elif two[i] =="#":
            two_num=two_num*-1
    for i in range(len(three)):
        if three[i] in dart_int:
            if three[0]=="1" and three[i]=="0":
                    three_num=10
                
                    
            else:
                
                three_num=int(three[i])
                        
        elif three[i] =="S":
            three_num=three_num
        elif three[i] =="D":
            three_num=three_num*three_num
        elif three[i] =="T":
            three_num=three_num*three_num*three_num
        elif three[i] =="*":
            two_num=two_num*2
            three_num=three_num*2
        elif three[i] =="#":
            three_num=three_num*-1
    answer=one_num+two_num+three_num
    return answer
dartResult="1S2D*3T"
        
dart_int=["0","1","2","3","4","5","6","7","8","9"]

answer=0
one=[dartResult[0]]
two=[]
three=[]
count=0
for i in range(1,len(dartResult)):
    if dartResult[i] in dart_int:
        if dartResult[i]=="0" and dartResult[i-1]=="1":
            count=count
        else:
            count=count+1
    if count==0:
        one.append(dartResult[i])
    elif count==1:
        two.append(dartResult[i])
    else:
        three.append(dartResult[i])
one_num=0
two_num=0
three_num=0
for i in range(len(one)):
    if one[i] in dart_int:
        if one[0]=="1" and one[i]=="0":
                one_num=10
            
                
        else:
            
            one_num=int(one[i])
                    
    elif one[i] =="S":
        one_num=one_num
    elif one[i] =="D":
        one_num=one_num*one_num
    elif one[i] =="T":
        one_num=one_num*one_num*one_num
    elif one[i] =="*":
        one_num=one_num*2
    elif one[i] =="#":
        one_num=one_num*-1
    
for i in range(len(two)):
    if two[i] in dart_int:
        if two[0]=="1" and two[i]=="0":
                two_num=10
            
                
        else:
            
            two_num=int(two[i])
                    
    elif two[i] =="S":
        two_num=two_num
    elif two[i] =="D":
        two_num=two_num*two_num
    elif two[i] =="T":
        two_num=two_num*two_num*two_num
    elif two[i] =="*":
        one_num=one_num*2
        two_num=two_num*2
    elif two[i] =="#":
        two_num=two_num*-1
for i in range(len(three)):
    if three[i] in dart_int:
        if three[0]=="1" and three[i]=="0":
                three_num=10
            
                
        else:
            
            three_num=int(three[i])
                    
    elif three[i] =="S":
        three_num=three_num
    elif three[i] =="D":
        three_num=three_num*three_num
    elif three[i] =="T":
        three_num=three_num*three_num*three_num
    elif three[i] =="*":
        two_num=two_num*2
        three_num=three_num*2
    elif three[i] =="#":
        three_num=three_num*-1
