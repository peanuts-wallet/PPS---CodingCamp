def solution(N, stages):
    answer = []
    players = len(stages)

    for stage in range(1, N + 1):
        failed = stages.count(stage)
        if players == 0:
            failure_rate = 0
        else:
            failure_rate = failed / players
        answer.append((stage, failure_rate))

        players -= failed
    answer.sort(key=lambda x: (-x[1], x[0]))
    return [stage for stage, rate in answer]