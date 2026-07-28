# A159 바탕화면 정리
def solution(wallpaper):
    min_row = len(wallpaper)
    min_column = len(wallpaper[0])
    max_row = 0
    max_column = 0

    for row in range(len(wallpaper)):
        for column in range(len(wallpaper[row])):
            if wallpaper[row][column] == '#':
                min_row = min(min_row, row)
                min_column = min(min_column, column)
                max_row = max(max_row, row + 1)
                max_column = max(max_column, column + 1)

    return [min_row, min_column, max_row, max_column]
