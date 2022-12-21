# 3. Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

user_number = int(input('Enter the number: '))
my_list = list(range(user_number+1))
summ = 0
for i in range(1, user_number+2):
    my_list[i-1] = round((1 + 1 / i) ** i, 3)
    summ += my_list[i-1]
print(my_list)
print(f'\nSumma = {summ}')

