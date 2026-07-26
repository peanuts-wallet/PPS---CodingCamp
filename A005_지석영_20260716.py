# A005 스킬트리
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        required_skills = ""

        # 선행 순서에 포함된 스킬만 남김
        for current_skill in skill_tree:
            if current_skill in skill:
                required_skills += current_skill

        # 남은 스킬 순서가 skill의 앞부분과 같아야 함
        if skill.startswith(required_skills):
            answer += 1

    return answer
