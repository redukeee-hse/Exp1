print("Hello, Git!")
print("Введите 2 числа через пробел:")
ListOfNumbers = [int(x) for x in input().split()]
print("Произведение чисел равно", ListOfNumbers[0] * ListOfNumbers[1])
print("Частное числа", ListOfNumbers[0], "от числа", ListOfNumbers[1], "равна", ListOfNumbers[0] / ListOfNumbers[1])