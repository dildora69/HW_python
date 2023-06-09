# Требуется найти в массиве A[1..N] самый
# близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

print("Hello! This is a program that finds the closest number to the X from the range(list) of numbers")

from random import randint #The randint() method returns an integer number selected element from the specified range.
num = int(input("Now please Enter the size of a list: "))
list_ofNumbers = [randint(1, 100) for _ in range(num)]
print(f"The list of Numbers is -> {list_ofNumbers}")

num2 = int(input("Enter the number X: "))
closest = min(list_ofNumbers, key=lambda x: abs(x - num2))
print(f"The closest number to the number {num2} is -> {closest}")