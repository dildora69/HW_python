print("Hello this is a program that calculates the sum of digits of a three-digit number")

num = int(input('Please Enter a number: '))
if 0 <= num < 1000:
    print(num)
    n1 = int(num / 100)
    n2 = int((num / 10) % 10)
    n3 = int(num % 10)
    sum = n1 + n2 + n3
    print(f' The sum of the digits of a number {num} -> {n1} + {n2} + {n3} = {sum}')
else: print("Please enter only positive and 3 digit number")
