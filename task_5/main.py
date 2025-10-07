a = input('Числа через пробел: ')
b = [int(x) for x in a.split()]
total = 0
for num in b:
    total += num
print('Введенные числа: ', b)
print('Сумма всех чисел: ', total)