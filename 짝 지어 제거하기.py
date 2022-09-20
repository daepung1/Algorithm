"""
짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작합니다.
 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다.
  그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다. 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다.
  문자열 S가 주어졌을 때, 짝지어 제거하기를 성공적으로 수행할 수 있는지 반환하는 함수를 완성해 주세요.
성공적으로 수행할 수 있으면 1을, 아닐 경우 0을 리턴해주면 됩니다.

예를 들어, 문자열 S = baabaa 라면

b aa baa → bb aa → aa →

의 순서로 문자열을 모두 제거할 수 있으므로 1을 반환합니다.

문제 풀이 후기: 스택을 사용해야만 풀 수 있는 문제였음 그냥 풀면 for문이나 재귀가 계속 돌아가야 하는데 스택을 쓰면 한번의 for문으로 결과가 나옴
"""
    
def solution(s):
    if len(s)==0:
        return 1
    elif len(s)==1:
        return 0
    else:
        keyword=''
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                keyword=s[i]
        try:
            s=s.replace(keyword,'',2)
            return solution(s)
        except:
            return 0   
print(solution("a"))
s="baabaa"
def solution(s):
    temp=[]
    for i in range(len(s)):
        temp.append(s[i])
        print(temp)
        if i!=0 and len(temp)>=2 and temp[-1]==temp[-2]:
            temp.pop()
            temp.pop()
    if len(temp)==0:
        return 1
    else:
        return 0