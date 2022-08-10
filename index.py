my_list = list()
i = 1
counter = 0
while i in range(1000):
    temp = i
    while temp > 0:
        value = temp % 10
        if value == 7:
            counter += 1
        temp = temp // 10
    i += 1

print(counter)