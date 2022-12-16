# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# *Пример:*
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

user_number = int(input('Enter the number: '))
N_list = list(range(1, user_number+1))
new_list = list(range(1, user_number+1))

for i in N_list:
    if i >=2:
        break
    else:
        for j in range(1, user_number+1):
            N_list[i-1] *= j
            new_list[j-1] = N_list[i-1]
            # print(f'i = {i}, j = {j}, N_list[{j}] = {N_list[i-1]}')
print(f'N = {user_number} -> {new_list}')
        
