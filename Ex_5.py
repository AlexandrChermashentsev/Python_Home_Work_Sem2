# 5. Реализуйте алгоритм перемешивания списка.

import random


number = random.randint(5, 10)
print(number)
list_my2 = {}
for i in range(1, number+1):
    list_my2[i] = random.randint(-9, 9)
print('old list: ', end='')
for v in list_my2:
    print(list_my2[v], end=' ')
print()


new_list = []
while list_my2 != {}:
    new_random_number = random.randint(1, number)
    if new_random_number in list_my2.keys():
        new_list.append(list_my2[new_random_number])
        del list_my2[new_random_number]
print('new list: ', end='')
print(*new_list)
