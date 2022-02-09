"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(n: int, sequence='', current=1):
    if current <= n:
        return triangular_sequence(
            n,
            sequence + str(current) * current + "\n",
            current + 1
        )
    else:
        return sequence
