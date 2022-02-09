"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(n: int) -> int:
    if n == 0:
        return 0
    return n % 10 + sum_of_numbers(n // 10)
