import math

#Половинное деление
def polovin(x0, x1, E):

    def func(x):
        return round(x ** 2 - math.sin(5 * x), 10)

    print(f'Длинна отрезка [x0, x1] = {abs(round(x1 - x0, 10))}')
    x0 = round(x0, 10)
    x1 = round(x1, 10)
    if abs(x1 - x0) < E:
        print(f'{x1=}')
        return

    x2 = round(0.5 * (x0 + x1), 10)
    print(f'{x0=}')
    print(f'{x1=}')
    print(f'{x2=}')
    print(f'f(x0) * f(x2) = {round(func(x0) * func(x2), 10)}')
    if func(x0) * func(x2) <= 0:
        polovin(x0, x2, E)

    else:
        polovin(x1, x2, E)

#Хорды
def hordi(x0, x1, E):
    def func(x):
        return round(x ** 2 - math.sin(5 * x), 10)

    print(f'Длинна отрезка [x0, x1] = {abs(x1 - x0)}')
    if abs(x1 - x0) >= E:
        x2 = round(x0 - ((x1 - x0) * func(x0)) / (func(x1) - func(x0)), 15)
        print(f'{x2=}')
        print(f'(x0) = {func(x0)}, f(x2) = {func(x2)}')
        print(f'(x2) = {func(x2)}, f(x1) = {func(x1)}')
        if (func(x0) < 0 and func(x2) > 0) or (func(x0) > 0 and func(x2) < 0):
            hordi(x2, x1, E)
        elif (func(x1) < 0 and func(x2) > 0) or (func(x1) > 0 and func(x2) < 0):
            hordi(x0, x2, E)
    else:
        print("END")

#Ньютона касательных
def nuton_cas(x0, x1, E):
    def f(x):
        return -x ** 3 - 2 * x ** 2 - 4 * x + 10

    def df(x):
        return -3 * x ** 2 - 4 * x - 4
    while 1:
        if df(x1) != 0:
            print(f'Значение производной функции в точке приближения = {df(x1)}')
            x1 = x1 - f(x1) / df(x1)
            print(f'Точка приближения = {x1}')
        else:
            break
        print(f'Длинна отрезка = {abs(x1 - x0)}')
        if abs(x1 - x0) < E:
            print(f'Приближенное значение х = {round(x1, 6)}')
            break
        x0 = x1


#Метод зейделя для СЛАУ(менять матрицу)
def zeidel(x1, x2, x3, E):
    mas = [[4.1, 5.8, -1.7, 0.8], [2.7, 3.3, 1.3, 2.1], [3.5, -1.7, 2.8, 1.7]]
    new_x1 = round((mas[0][3] - mas[0][0] * x1 - mas[0][1] * x2 - mas[0][2] * x3) / mas[0][0] + x1, 6)
    new_x2 = round((mas[1][3] - mas[1][0] * new_x1 - mas[1][1] * x2 - mas[1][2] * x3) / mas[1][1] + x2, 6)
    new_x3 = round((mas[2][3] - mas[2][0] * new_x1 - mas[2][1] * new_x2 - mas[2][2] * x3) / mas[2][2] + x3, 6)
    print(f'{new_x1=}, {new_x2=}, {new_x3=}')
    print(f'x1\' - x1 =' f'{round(abs(new_x1 - x1), 3)} >= {E}')
    print(f'x2\' - x2 =' f'{round(abs(new_x2 - x2), 3)} >= {E}')
    print(f'x3\' - x3 =' f'{round(abs(new_x3 - x3), 3)} >= {E}')
    if abs(new_x1 - x1) < E and abs(new_x2 - x2) < E and abs(new_x3 - x3) < E:
        print(f'{new_x1=}, {new_x2=}, {new_x3=}')
        return
    else:
        zeidel(new_x1, new_x2, new_x3, E)

#Метод трапеций для функции
def integral(a, b, h):
    sum = 0
    count = abs(b-a) / h
    print(f'{count=}')
    R = -(h**3)/12 * 1.5374   #Второй множитель - интеграл (a,b) от f''
    print(f'{R=}')
    def f(x):
        return x * math.log(x, math.e)**2

    for i in range(int(count) + 1):
        if i == 0 or i == count:
            sum += 0.5 * f(a + h * i)
            print(f'f({a + h * i}) = {f(a + h * i)}')
        else:
            sum += f(a + h * i)
            print(f'f({a + h * i}) = {f(a + h * i)}')
            print(sum)
    print(f'Интеграл = {h * sum + R}')

def mid(a, b, h):
    sum = 0
    count = abs(b - a) / h
    print(f'{count=}')
    R = h**2/24 * 1.5374   #Второй множитель - интеграл (a,b) от f''
    print(f'{R=}')
    def f(x):
        return x * math.log(x, math.e)**2

    for i in range(1, int(count) + 1):
        sum += f(a - h/2 + h * i)
        print(f'f({a - h/2 + h * i}) = {f(a - h/2 + h * i)}')
    print(f'Интеграл = {h * sum + R}')

def left_or_right(a, b, h, pos):
    sum = 0
    count = abs(b - a) / h
    print(f'{count=}')
    R = h/2 * 1.5785   #Второй множитель - интеграл (a,b) от f'
    print(f'{R=}')
    def f(x):
        return x * math.log(x, math.e) ** 2

    if pos == 'left':
        for i in range(int(count)):
            sum += f(a + h * i)
            print(f'f({a + h * i}) = {f(a + h * i)}')
    elif pos == 'right':
        for i in range(1, int(count) + 1):
            sum += f(a + h * i)
            print(f'f({a + h * i}) = {f(a + h * i)}')
    print(f'Интеграл = {h * sum + R}')

def simpson(a, b, h):
    sum = 0
    count = abs(b - a) / h
    print(f'{count=}')
    R = -(h**4)/180 * 0.1024 #Второй множитель - интеграл (a,b) от f''''
    print(f'{R=}')
    def f(x):
        return x * math.log(x, math.e) ** 2
    print(f'f({a}) = {f(a)}')
    for i in range(1, int(count), 2):
        sum += 4 * f(a + h * i)
        print(f'f({a + h * i}) = {f(a + h * i)}')
    for j in range(2, int(count) - 1, 2):
        sum += 2 * f(a + h * j)
        print(f'f({a + h * j}) = {f(a + h * j)}')
    sum += f(a) + f(b)
    print(f'f({b}) = {f(b)}')
    print(h/3 * sum + R)


import numpy as np
def function(xy):
    x, y = map(float, xy.tolist())
    return x + np.cos(y / 3)
y0 = 4.6
h = 0.1
t = [1.6 + i / 10 for i in range(11)]
print('Метод Эйлера')
def euler(xy, h=0.1, n=10000):
    x = xy[0]
    xy[0] = 0.
    while x - xy[0] > 0:
        xy = xy + np.array([h, h * function(xy)])
    return xy
for x in t:
    fxy = np.array([x, y0])
    print('x = {:.1f} y = {:.3f}'.format(*map(float, euler(fxy, h).tolist())))

if __name__ == '__main__':
    #polovin(0.5, 1, 0.000001)   #Указывать промежуток с 1 корнем
    #hordi(0.5, 1, 0.000001)   #Указывать промежуток с 1 корнем
    nuton_cas(0, 2, 0.000001)
    #zeidel(0, 0, 0, 0.000001)
    #integral(2,3,0.01)
    #mid(2,3,0.01)
    #left_or_right(2, 3, 0.01, 'left')
    #left_or_right(2, 3, 0.01, 'right')
    #simpson(2, 3, 0.01)
