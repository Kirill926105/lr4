numbers = [] # kirill kulbitskiy, ввод чисел в список
print("Введи числа: ")

while True: # цикл для ввода чисел
    n = input()
    if n == "": # нажать Enter после ввода числа для окончания списка
        break
    numbers.append(int(n))

# Считаем сумму
sum = 0
for x in numbers:
    sum = sum + x

# Выводим результаты
print("Твои числа:", numbers)
print("Сумма чисел:", sum)