"""
HW 3-2
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов
"""
from random import randint

len_original_lst = 15

original_lst = []
for _ in range(len_original_lst):
    original_lst.append(randint(0, 10))
print(original_lst)

result_list = []
for item in original_lst:
    if original_lst.count(item) > 1 and item not in result_list:
        result_list.append(item)
print(result_list)