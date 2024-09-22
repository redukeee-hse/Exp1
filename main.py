print("Hello, Git!")
print("Введите 2 числа через пробел:")
ListOfNumbers = [int(x) for x in input().split()]
num1 = ListOfNumbers[0]
num2 = ListOfNumbers[1]
print("Произведение чисел равно", num1 * num2)
print("Частное числа", num1, "от числа", num2, "равна", num1 / num2)
print("Сумма чисел равна", num1 - num2)
print("Разность чисел", num1, "и", num2, "равна", num1 + num2)
print("Где-то ошибка -_-")
