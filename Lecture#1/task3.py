num = int(input('Please Enter the number of the ticket:  '))
n = int(num / 1000)
n3 = int(n / 100)
n2 = int((n / 10) % 10)
n1 = int(n % 10)
sum1 = n1 + n2 + n3

num2 = int(num % 1000)
n4 = int(num2 / 100)
n5 = int((num2 / 10) % 10)
n6 = int(num2 % 10)
sum2 = n4 + n5 + n6
if sum1 == sum2:
    print(f'Sum of first 3 digits {n} -> {n3} + {n2} + {n1} = {sum1}')
    print(f'Sum of second 3 digits {num2} -> {n4} + {n5} + {n6} = {sum2}')
    print(f'Yes!!! You have the lucky ticket -> {sum1} = {sum2}')
else:
    print('Sorry No :(  But it is an ordinary ticket')




