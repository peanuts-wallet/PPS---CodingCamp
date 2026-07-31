def solution(wallpaper):
    xs = []
    ys = []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                xs.append(i)
                ys.append(j)

    return [min(xs), min(ys), max(xs) + 1, max(ys) + 1]