# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую
# степень B с помощью рекурсии.

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))


def rec_pow(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / a * rec_pow(a, b + 1)
    return a * rec_pow(a, b - 1)


print(f" {a}^{b} -> {rec_pow(a, b)}")
