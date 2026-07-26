# A011 실패율
def solution(N, stages):
    stage_counts = [0] * (N + 2)

    # 각 스테이지에 머무르는 사용자 수 계산
    for stage in stages:
        stage_counts[stage] += 1

    remaining_users = len(stages)
    failure_rates = []

    for stage in range(1, N + 1):
        if remaining_users == 0:
            failure_rate = 0
        else:
            failure_rate = stage_counts[stage] / remaining_users

        failure_rates.append((stage, failure_rate))
        remaining_users -= stage_counts[stage]

    # 실패율 내림차순, 같으면 스테이지 번호 오름차순
    failure_rates.sort(key=lambda value: (-value[1], value[0]))

    answer = []

    for stage, failure_rate in failure_rates:
        answer.append(stage)

    return answer
