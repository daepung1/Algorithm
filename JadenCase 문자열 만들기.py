"""
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
 단, 첫 문자가 알파벳이 아닐 때에는 이어지는 알파벳은 소문자로 쓰면 됩니다. 
 (첫 번째 입출력 예 참고)
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.
"""
def solution(s):
    answer = ''
    return answer
s="3people unFollowed me"
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big_alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha_check=alpha+big_alpha
check=0
answer=''
for i in range(len(s)):
    if i==0 and s[i] in alpha_check:
        answer=answer+s[i].upper()
    elif check==1:
        answer=answer+s[i].upper()
        check=0
    else:
        answer=answer+s[i].lower()
    if s[i]==" ":  
        check=1
print(answer)    


        