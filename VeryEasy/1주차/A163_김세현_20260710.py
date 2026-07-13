def solution(today, terms, privacies):
    answer = []

    today_year, today_month, today_day = map(int, today.split("."))
    today_total = today_year * 12 * 28 + today_month * 28 + today_day

    term_dict = {}

    for term in terms:
        term_type, period = term.split()
        term_dict[term_type] = int(period)

    for i, privacy in enumerate(privacies):
        date, term_type = privacy.split()

        year, month, day = map(int, date.split("."))
        collected_total = year * 12 * 28 + month * 28 + day

        expiration_date = collected_total + term_dict[term_type] * 28

        if expiration_date <= today_total:
            answer.append(i + 1)

    return answer