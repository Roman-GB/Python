# 7. По длинам трех отрезков, введенных пользователем, определить возможность
# существования треугольника, составленного из этих отрезков. Если такой треугольник существует,
# то определить, является ли он разносторонним, равнобедренным или равносторонним.
print('Введите длины сторон треугольника')
x = int(input("\tДлина 1-ой стороны: "))
y = int(input("\tДлина 2-ой стороны: "))
z = int(input("\tДлина 3-ей стороны: "))

if x + y > z and x + z > y and y + z > x:
    print('Треугольник существует')
else:
    print('Треугольник не существует')

if x == y and y == z:
    print('Треугольник равносторонний')
elif x == y or y == z or x == z:
    print('Треугольник равнобедренный')
elif x != y and y != z:
    print('Треугольник разносторонний')

