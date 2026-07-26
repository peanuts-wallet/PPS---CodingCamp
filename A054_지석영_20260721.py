# A054 크레인 인형뽑기 게임
def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        column = move - 1

        for row in range(len(board)):
            if board[row][column] != 0:
                doll = board[row][column]
                board[row][column] = 0

                if basket and basket[-1] == doll:
                    basket.pop()
                    answer += 2
                else:
                    basket.append(doll)

                break

    return answer
