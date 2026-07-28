# A158 달리기 경주
def solution(players, callings):
    positions = {}

    for index in range(len(players)):
        positions[players[index]] = index

    for called_player in callings:
        current_index = positions[called_player]
        front_player = players[current_index - 1]

        players[current_index - 1] = called_player
        players[current_index] = front_player

        positions[called_player] = current_index - 1
        positions[front_player] = current_index

    return players

