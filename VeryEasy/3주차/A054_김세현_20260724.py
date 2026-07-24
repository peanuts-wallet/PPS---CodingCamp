def solution(board, moves):
    answer = 0
    tmp = 0
    bucket = [] # 인형뽑기가 집은 인형 담는 리스트
    for index in moves:
        for i in range(len(board)):
            if board[i][index-1] != 0:
                tmp = board[i][index-1]
                board[i][index-1] = 0
                if len(bucket) == 0: # 아예 비어있으면 무시
                    bucket.append(tmp)
                elif bucket[-1] == tmp: # 중복 발견
                    del bucket[-1]
                    answer += 2
                else:
                    bucket.append(tmp)
                break
    return answer
# 먼저 가장 위부터 0이 아닌 수가 있는지 판단해서 잡을 높이를 구한다.
# 잡은 수는 tmp에 저장한다. 고른 숫자가 있던 인덱스 요소는 0으로 바꾼다.
# 중복 시, 터지는 조건 : 고른 수가 바구니의 마지막 원소([-1])와 값이 같다면 del[-1]한다.
# 추가로 answer += 2 한다.
# 그게 아니라면 append로 넣는다.
