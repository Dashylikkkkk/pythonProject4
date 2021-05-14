import random


def generate_password(num):
    used = ['0', 'o', 'O', '1', 'I', 'l']
    answer = ''
    check = False
    while not check:
        answer = ''
        upper = False
        lower = False
        number = False
        while len(answer) != num:
            a = random.randint(48, 122)
            sign = chr(a)
            if sign not in used and not (65 > a > 57 or 97 > a > 90):
                if sign.isupper():
                    upper = True
                elif sign.islower():
                    lower = True
                elif sign.isdigit():
                    number = True
                answer += sign
        if upper and lower and number:
            check = True
    return answer


def main(amount, num):
    answer = []
    for i in range(amount):
        answer.append(generate_password(num))
    return answer


print("Случайный пароль из 7 символов:" , generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")