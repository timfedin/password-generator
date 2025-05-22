import random

length = int(input("Длина пароля (рекомендуется 12+): "))
numbers = input("Включать цифры?(введите y или n):")
special = input("Включать специальные символы?(введите y или n): ")

if numbers == 'y':
    numbers = True
else:
    numbers == False

if special == 'y':
    special = True    
else:
    special = False

def passwordgen(length, numbers, special):
    lowercase = 'qwertyuiopasdfghjklzxcvbnm'
    appercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    chisl = '1234567890'
    spec = '!@#$%^&*()_+|[/.,]'

    osnov = lowercase + appercase

    if numbers == True:
        osnov += chisl

    if special == True:
        osnov += spec
    
    password = []
    for i in range(length):
        password.append(random.choice(osnov))
    
    return ''.join(password)

password = passwordgen(length, numbers, special)
print('вот ваш пароль: ' +password)