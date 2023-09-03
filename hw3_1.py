"""
HW 3-1
Три друга взяли вещи в поход.
Сформируйте словарь, где
ключ — имя друга, а
значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.
"""
from random import randint

friends = ['Bob', 'Alex', 'Tom']
things = ['water', 'tent', 'flashlight', 'food', 'first aid kit', 'sleeping bag', 'knife', 'navigator']

team = dict()
things_in_bag = 3

for friend in friends:
    person_kit = []
    while len(person_kit) < things_in_bag:
        thing = things[randint(0, len(things) - 1)]
        if thing not in person_kit:
            person_kit.append(thing)
    team.update({friend: tuple(person_kit)})

print(team)

two_person_kit = set()

print()
team_things = set()
for value in team.values():
    for item in value:
        team_things.add(item)
print(*friends, sep=', ', end=' ')
print('took', end=' ')
print(*team_things, sep=', ', end='.\n')

print()
unique_things = set()
for person in team.keys():
    unique_things = set(team.get(person))
    for key, value in team.items():
        if key != person:
            unique_things = unique_things - set(team.get(key))
            for item in value:
                two_person_kit.add(item)
            two_person_kit = two_person_kit - unique_things
    if len(unique_things) == 0:
        print(person, 'has not any unique thing,', end=' ')
        print('and other friends have', end=' ')
        print(*two_person_kit, sep=', ', end='.\n')
    elif len(unique_things) == 1:
        print(person, 'has unique thing:', *unique_things, end=', but ')
        print('other friends have', end=' ')
        print(*two_person_kit, sep=', ', end='.\n')
    else:
        print(person, 'has unique things:', end=' ')
        print(*unique_things, sep=', ', end=', but ')
        print('other friends have', end=' ')
        print(*two_person_kit, sep=', ', end='.\n')
