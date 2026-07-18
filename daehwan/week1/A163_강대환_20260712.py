def solution(today, terms, privacies):
    answer = []
    
    def date_to_days(date):
        year, month, day = map(int, date.split("."))
        return year * 12 * 28 + month * 28 + day
    
    today_days = date_to_days(today)
    
    term_dict = {}
    for term in terms:
        kind, month = term.split()
        term_dict[kind] = int(month)
    
    for i in range(len(privacies)):
        date, kind = privacies[i].split()
        
        start_days = date_to_days(date)
        expire_days = start_days + term_dict[kind] * 28
        
        if expire_days <= today_days:
            answer.append(i + 1)
    
    return answer