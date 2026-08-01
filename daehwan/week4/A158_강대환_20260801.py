def solution(players, callings):
    answer = []
    
    rank = {}
    
    for i in range(len(players)):
        rank[players[i]] = i
    
    for name in callings:
        current_index = rank[name]
        front_index = current_index - 1
        
        front_player = players[front_index]
        
        players[front_index], players[current_index] = players[current_index], players[front_index]
        
        rank[name] = front_index
        rank[front_player] = current_index
    
    answer = players
    
    return answer