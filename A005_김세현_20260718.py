def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        filtered = ""
        for current_skill in tree:
            if current_skill in skill:
                filtered += current_skill
        if filtered == skill[:len(filtered)]:
            answer += 1

    return answer