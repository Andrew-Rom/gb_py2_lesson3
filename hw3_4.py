"""
HW 3-4
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""
import random

max_capacity = 14

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

bug_versions = []

repeat = 0

while 0 <= repeat <= 100000:

    bug = set()
    bug_weight = 0

    while bug_weight <= max_capacity:

        things_for_packing = []
        for key in things.keys():
            if things.get(key) < (max_capacity - bug_weight) and key not in bug:
                things_for_packing.append(key)

        if len(things_for_packing) > 0:
            thing = random.choice(things_for_packing)
            if (bug_weight + things.get(thing)) <= max_capacity:
                bug.add(thing)
                bug_weight += things.get(thing)
        else:
            break

    if len(bug_versions) > 0:
        unique_kit = True
        while unique_kit:
            for bug_version in bug_versions:
                if len(bug - bug_version) == 0:
                    unique_kit = False
                    repeat += 1
                    break
            break
        if unique_kit:
            bug_versions.append(bug)
    else:
        bug_versions.append(bug)

print(*bug_versions, sep='\n')
