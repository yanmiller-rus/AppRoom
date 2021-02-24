def get_square_area():
    print("Введите сторону")
    a = int(input())
    S = a ** 2
    print("Площадь комнаты равна %s кв.м" % S)


def get_square_rectangle():
    print("Введите длину")
    a = int(input())
    print("Введите ширину")
    b = int(input())
    S = a*b
    print("Площадь комнаты равна %s кв.м" % S)


def get_square_triangle():
    print("Введите сторону 1")
    a = int(input())
    print("Ввведите сторону 2")
    b = int(input())
    print("Введите сторону 3")
    c = int(input())
    p = (a+b+c) // 2
    S = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    print("Площадь комнаты равна %s кв.м" % S)


def get_square_circle():
    print("Введите радиус комнаты")
    r = int(input())
    S = 3.14 * (r**2)
    print("Площадь комнаты равна %s кв.м" % S)


print("Программа для нахождения площади по типу фигуры")
print("=============================")
print("Введите фигуру вашей комнаты!")
print("==============================")
request = input()
if request == 'квадрат':
    print(get_square_area())
elif request == 'прямоугольник':
    print(get_square_rectangle())
elif request == 'треугольник':
    print(get_square_triangle())
elif request == 'круг':
    print(get_square_circle())
