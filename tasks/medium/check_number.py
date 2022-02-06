"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n) -> bool:
    if n <= 0:
        return False
    if n == 1:
        return True
    return n & 1 == 0 and check_number(n // 2)
