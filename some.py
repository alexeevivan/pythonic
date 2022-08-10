a = [200, 300, 400, 600, 500, 100, 700, 900, 800, 4]
min_value = a[0]
for i in range(len(a)):
    if min_value >= a[i]:
        min_value = a[i]
print(min_value)