"""
HW 3-4
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

bug_capacity = 14

things = {'water': 4,
          'tent': 9,
          'flashlight': 2,
          'food': 5,
          'first aid kit': 3,
          'sleeping bag': 7,
          'knife': 2,
          'navigator': 3,
          'matchsticks': 1,
          'map': 1,
          'compass': 1,
          'camera': 3,
          'radio': 4}

bug = dict()
bug_weight = 0

things_for_packing = things.copy()

for key, value in things.items():
    if (bug_weight + value) <= bug_capacity and key in things_for_packing.keys():
        bug.update({key: things_for_packing.pop(key)})
        bug_weight += value
print(bug)
