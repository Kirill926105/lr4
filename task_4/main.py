n = int(input('n: ')) # kirill kulbitskiy, ввод числа
n2 = [x for x in range(1, n + 1) if x % 5 == 0] # список из чисел которые / на 5 без остатка, в последовательности от 1 до числа n
print(n2)