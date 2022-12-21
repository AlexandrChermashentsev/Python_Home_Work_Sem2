# 4. Задайте список из N элементов,
# заполненных РАНДОМНЫМИ числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

user_number = int(input('Enter the number: '))
my_dict = {}
for i in range(1, user_number+1):
    my_dict[i] = random.randint(-user_number, user_number)
print(my_dict)

user_key_1 = int(input('Enter the first key: '))
user_key_2 = int(input('Enter the second key: '))
multiplication = my_dict[user_key_1] * my_dict[user_key_2]
print(multiplication)

with open('file.txt', 'w') as data:
    data.write(f'keys: {user_key_1}, {user_key_2}\
        key values: {my_dict[user_key_1]}, {my_dict[user_key_2]}\
        multiplying your key values = {multiplication}')