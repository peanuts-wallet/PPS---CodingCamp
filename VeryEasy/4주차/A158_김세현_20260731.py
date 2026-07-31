def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}

    for player in callings:
        i = rank[player]
        front = players[i - 1]

        players[i - 1], players[i] = players[i], players[i - 1]
        rank[player] -= 1
        rank[front] += 1

    return players