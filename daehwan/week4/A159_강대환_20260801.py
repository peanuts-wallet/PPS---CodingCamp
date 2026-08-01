def solution(wallpaper):
    answer = []
    
    lux = 51
    luy = 51
    rdx = 0
    rdy = 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                lux = min(lux, i)
                luy = min(luy, j)
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)
    
    answer = [lux, luy, rdx, rdy]
    
    return answer