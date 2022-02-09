"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(num_list: list):
    num_before = set()
    for num in num_list:
        if num in num_before:
            print('Yes')
        else:
            print('No')
            num_before.add(num)


yes_or_no([1, 2, 3, 4, 6, 3, 5, 7])
