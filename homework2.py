# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

print('ввести координаты не равные 0')
х = int(input('Введите число x:'))
y = int(input('Введите число y:'))
if х == 0 or y == 0:
    print('введены некорректные значения')
if х > 0 and y > 0:
    print('1')
elif х < 0 and y > 0:
    print('2')
elif х < 0 and y < 0:
    print('3')
elif х > 0 and y < 0:
    print('4')
