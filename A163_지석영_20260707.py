# A163 개인정보 수집 유효기간
def solution(today, terms, privacies):
    answer = []
    term_months = {}

    # 오늘 날짜를 일수로 변환
    today_year, today_month, today_day = map(int, today.split("."))
    today_total = today_year * 12 * 28 + today_month * 28 + today_day

    # 약관 종류별 유효기간 저장
    for term in terms:
        term_type, month = term.split()
        term_months[term_type] = int(month)

    for index in range(len(privacies)):
        date, term_type = privacies[index].split()
        year, month, day = map(int, date.split("."))

        collected_total = year * 12 * 28 + month * 28 + day
        expiration_total = collected_total + term_months[term_type] * 28

        # 유효기간이 지난 개인정보 번호 추가
        if expiration_total <= today_total:
            answer.append(index + 1)

    return answer

