def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    s = s.lower()
    countF = s.count('p')
    countY = s.count('y')
    if(countF != countY):
        answer = False
    return answer