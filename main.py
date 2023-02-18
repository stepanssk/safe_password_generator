from random import choice

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

cnt_passw = int(input('Specify the number of passwords to generate:'))
len_passw = int(input('Specify the length of one password:'))
add_digits = input('Include numbers 0123456789? (y/n)').strip()
add_upper = input('Include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)').strip()
add_lower = input('Include lowercase letters abcdefghijklmnopqrstuvwxyz? (y/n)').strip()
add_punct = input('Include symbols !#$%&*+-=?@^_? (y/n)').strip()
remove_symbols = input('Exclude ambiguous characters il1Lo0O? (y/n)').strip()

if add_digits.lower() == 'y':
    chars += digits
if add_lower.lower() == 'y':
    chars += lowercase_letters
if add_upper.lower() == 'y':
    chars += uppercase_letters
if add_punct.lower() == 'y':
    chars += punctuation
if remove_symbols.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(len_passw, chars):
    password = ''
    for _ in range(len_passw):
        password += choice(chars)
    return password

for _ in range(cnt_passw):
    print(generate_password(len_passw, chars))
