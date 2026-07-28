# A177 최소직사각형
def solution(sizes):
    maximum_width = 0
    maximum_height = 0

    for width, height in sizes:
        longer_side = max(width, height)
        shorter_side = min(width, height)

        maximum_width = max(maximum_width, longer_side)
        maximum_height = max(maximum_height, shorter_side)

    return maximum_width * maximum_height

