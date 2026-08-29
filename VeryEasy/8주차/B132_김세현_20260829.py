from collections import deque


def solution(maps):
    row_count = len(maps)
    column_count = len(maps[0])
    visited = [[False] * column_count for _ in range(row_count)]
    visited[0][0] = True
    queue = deque([(0, 0, 1)])

    while queue:
        row, column, distance = queue.popleft()

        if row == row_count - 1 and column == column_count - 1:
            return distance

        for row_offset, column_offset in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next_row = row + row_offset
            next_column = column + column_offset

            if not (0 <= next_row < row_count and 0 <= next_column < column_count):
                continue
            if visited[next_row][next_column] or maps[next_row][next_column] == 0:
                continue

            visited[next_row][next_column] = True
            queue.append((next_row, next_column, distance + 1))

    return -1
