def solution(n, computers):
    visited = [False] * n
    network_count = 0

    for start in range(n):
        if visited[start]:
            continue

        network_count += 1
        visited[start] = True
        stack = [start]

        while stack:
            computer = stack.pop()

            for neighbor, connected in enumerate(computers[computer]):
                if connected and not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)

    return network_count
