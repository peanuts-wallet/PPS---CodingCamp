# A141 전화번호 목록
def solution(phone_book):
    phone_book.sort()

    for index in range(len(phone_book) - 1):
        current_number = phone_book[index]
        next_number = phone_book[index + 1]

        if next_number.startswith(current_number):
            return False

    return True

