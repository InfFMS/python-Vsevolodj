# Задача 10: Уравнение прямой
# Напишите программу, которая находит значение y в уравнении прямой y = kx + b для заданных x, k и b.
# Пример:
# Ввод: k = 2, b = 3, x = 5
# Вывод: y = 13
value1, value2, value3 = map(int, input("Введите три числа:").split())
print("y =", value3*value1+value2)