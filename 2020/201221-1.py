# https://davinci-ai.tistory.com/32

def solution(phone_book):
    phone_book.sort(key=len)
    for i in range(0, len(phone_book)):
        len1 = len(phone_book[i])
        for j in range(i+1, len(phone_book)):
            if phone_book[i] == phone_book[j][:len1]:
                return True
    return False
phone_book = ["119", "97674223", "1195524421"]

print(solution(phone_book))