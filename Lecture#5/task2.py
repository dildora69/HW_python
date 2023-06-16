# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))


def rec_sum(a, b):
    if b > 0 and a > 0:
        return rec_sum(a + 1, b - 1)


print(rec_sum(a, b))
