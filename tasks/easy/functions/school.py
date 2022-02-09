"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""

school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}


def incr_students(school_data: dict, name_class: str) -> dict:
    for key, value in school_data.items():
        school_data[key] = value + 1
    return school_data


def decr_students(school_data: dict, name_class: str) -> dict:
    for key, value in school_data.items():
        school_data[key] = value - 1
    return school_data


def add_class(school_data: dict, name_class: str) -> dict:
    school_data.update({'3b': 0})
    return school_data


def remove_class(school_data: dict, name_class: str) -> dict:
    school_data.pop('1a')
    return school_data


def calc_students(school_data: dict) -> int:
    num_students = sum(school_data.values())
    return num_students
