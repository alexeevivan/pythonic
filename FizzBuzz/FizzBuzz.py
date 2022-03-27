for i in range(15, 30):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end='; ')
    elif i % 3 == 0:
        print("Fizz", end='; ')
    elif i % 5 == 0:
        print("Buzz", end='; ')
    else:
        print(i, end='; ')

print(i)