# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import choices
print("Hello this is a program that shows the number of chosen number in the list of random N numbers")
n = int(input("Now please the amount of number in the list: "))
list_ofNumbers = choices(range(n * 2), k = n)
print(f"The list o f number's are -> {list_ofNumbers}")
output = list_ofNumbers.count(int(input()))
print(output)
