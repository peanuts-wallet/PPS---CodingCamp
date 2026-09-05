import re


def solution(new_id):
    recommended_id = new_id.lower()
    recommended_id = re.sub(r"[^a-z0-9_.-]", "", recommended_id)
    recommended_id = re.sub(r"\.+", ".", recommended_id)
    recommended_id = recommended_id.strip(".")

    if not recommended_id:
        recommended_id = "a"

    recommended_id = recommended_id[:15].rstrip(".")

    while len(recommended_id) < 3:
        recommended_id += recommended_id[-1]

    return recommended_id
