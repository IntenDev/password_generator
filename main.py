from random import choice

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''
res_chars = ''
sum_pwd = int(input('Сколько паролей сгенирировать? (цифрами) - '))
len_pwd = int(input('Длинна одного пароля (цифрами) - '))
add_numbers = input('Включать ли цифры? (Да/Нет) - ')
add_uppers_letters = input('Включать ли прописные буквы? (Да/Нет) - ')
add_lowers_letters = input('Включать ли строчные буквы? (Да/Нет) - ')
add_simbols = input('Включать ли символы? (Да/Нет) - ')
del_ambiguous_symbols = input('Исключать ли неоднозначные символы - "il1Lo0O"? (Да/Нет) - ')

if add_numbers.lower() == 'да':
    chars += DIGITS
if add_uppers_letters.lower() == 'да':
    chars += UPPERCASE_LETTERS
if add_lowers_letters.lower() == 'да':
    chars += LOWERCASE_LETTERS
if add_simbols.lower() == 'да':
    chars += PUNCTUATION
if del_ambiguous_symbols.lower() == 'да':
    for i in range(len(chars)):
        if chars[i] not in 'il1Lo0O':
            res_chars += chars[i]
else:
    res_chars = chars


def generate_password(length, char):
    password = ''.join(choice(char) for _ in range(length))
    return password


for _ in range(sum_pwd):
    print(generate_password(len_pwd, res_chars))
