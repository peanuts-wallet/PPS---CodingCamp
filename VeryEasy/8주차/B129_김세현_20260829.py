def solution(routes):
    camera_position = -30001
    camera_count = 0

    for entry, exit_ in sorted(routes, key=lambda route: route[1]):
        if entry > camera_position:
            camera_position = exit_
            camera_count += 1

    return camera_count
