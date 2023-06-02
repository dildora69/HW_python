
p = int(input("Enter a number:  "))
if 0 <= p <= 50:
    s = p
    k = int(2*(p+s))
    print(f'{p} + {k} + {s} = {p+ k +s}')
else: print("Error! sorry but it's impossible for a person to make a paper bird more than 50 :)")