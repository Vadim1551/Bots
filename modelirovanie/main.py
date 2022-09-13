# 1 номер ----------------------------
import random
import math
from math import log10, floor

#ВЫЧИСЛЯЕМ ПИ
def CALC_PI(x0, y0, r0, ExpNmb):
    m = 0
    xmax, xmin = x0 + r0, x0 - r0
    ymax, ymin = y0 + r0, y0 - r0
    for i in range(0, ExpNmb):
        p1 = random.uniform(0, 1)
        p2 = random.uniform(0, 1)
        xp = (xmax - xmin) * p1 + xmin
        yp = (ymax - ymin) * p2 + ymin
        if (xp - x0) ** 2 + (yp - y0) ** 2 < r0 ** 2:
            m += 1
    pi = 4 * m / ExpNmb
    print(pi)
    return(pi)

# 2 номер -----------------------------------------------

#ЗАПИСЫВАЕМ РЕЗУЛЬТАТЫ ВЫЧИСЛЕНИЙ ПИ В СПИСОК(СЕРИЮ)
def SERIA_CALC(seria):
    for i in range(4, 9):
        seria.append(CALC_PI(1, 2, 5, 10 ** i))
    print('СЕРИЯ ВЫЧИСЛЕНА')

SERIA_1 = []
SERIA_2 = []
SERIA_3 = []
SERIA_4 = []
SERIA_5 = []
SERIES = [SERIA_1, SERIA_2, SERIA_3, SERIA_4, SERIA_5]

#ВЫВОДИМ ЗНАЧЕНИЯ НА ЭКРАН
for item in SERIES:
    SERIA_CALC(item)

# 3 номер ------------------------------------------------

#ОКРУГЛЯЕМ ПОГРЕШНОСТЬ ДО ПОСЛЕДНЕЙ ЗНАЧУЩЕЙ ЦИФРЫ
def round_to_1(x):
    return round(x, -int(floor(log10(abs(x)))))

#ВЫЧИСЛЯЕМ ПОГРЕШНОСТЬ
def pogrserii(seria, num):
    for i in range(0, 5):
        x1 = round_to_1(abs(math.pi - seria[i]))
        print(f"ПОГРЕШНОСТЬ ВЫЧИСЛЕНИЙ ЧИСЛА В СЕРИИ {num} ДЛЯ 10^{i + 4} ЭКСПЕРИМЕНТОВ = {x1}")

#ВЫВОДИМ ПОГРЕШНОСТЬ ВЫЧИСЛЕНИЙ ЗНАЧЕНИЙ ЧИСЛА ДЛЯ КАЖДОЙ СЕРИИ
pogrserii(SERIA_1, 1)
pogrserii(SERIA_2, 2)
pogrserii(SERIA_3, 3)
pogrserii(SERIA_4, 4)
pogrserii(SERIA_5, 5)

#ВЫЧИСЛЯЕМ И ВЫВОДИМ ПОГРЕШНОСТЬ ВЫЧИСЛЕНИЙ ДЛЯ УСРЕДНЕННЫХ ПО СЕРИЯМ ЗНАЧЕНИЙ
for i in range(0, 5):
    sredni = (SERIA_1[i] + SERIA_2[i] + SERIA_3[i] + SERIA_4[i] + SERIA_5[i]) / 5
    print(f"ПОГРЕШНОСТЬ ВЫЧИСЛЕНИЙ ДЛЯ УСРЕДНЕННЫХ ПО СЕРИЯМ ЗНАЧЕНИЙ ПРИ 10^{i+4} ЭКСПЕРИМЕНТОВ = {round_to_1(abs(math.pi - sredni))}")

# 4 номер --------------------------------------------------

#ОКРУГЛЯЕМ ПОГРЕШНОСТЬ ДО ПОСЛЕДНЕЙ ЗНАЧУЩЕЙ ЦИФРЫ
def round_1(x):
    return round(x, -int(floor(log10(abs(x)))))

#ВЫЧИСЛЕНИЯ ЗНАЧЕНИЯ ДАННОЙ НАМ ФУНКЦИИ
def F(x):
    return(x**3 + 1)

#ВЫЧИСЛЕНИЕ И ЗАПИСЬ ЗНАЧЕНИЙ ИНТЕГРАЛА В СЕРИЮ
def CALC(seria):
    for i in range(4, 8):
        x = integ(10**i)
        seria.append(x)

#ВЫЧИСЛЕНИЯ ЗНАЧЕНИЯ ИНТЕГРАЛА МЕТОДОМ МОНТЕ-КАРЛО
def integ(ExpNmb):
    a = 0
    b = 2
    sum = 0
    for i in range(0, ExpNmb):
        xi = a + random.uniform(0, 1) * (b - a)
        sum += F(xi)
    J = (b - a) / ExpNmb * sum
    print(J)
    return(J)

#ЗНАЧЕНИЕ ДАННОГО НАМ ИНТЕГРАЛА(АНАЛИТИЧЕСКОЕ)
funcValue = 6


SERIA1 = []
SERIA2 = []
SERIA3 = []
SERIESS = [SERIA1, SERIA2, SERIA3]

#ЗАПИСЬ ЗНАЧЕНИЯ ИНТЕГРАЛА МЕТОДОМ МОНТЕ-КАРЛО В СЕРИИ
for item in SERIESS:
    CALC(item)
    print("СЕРИЯ ВЫЧИСЛЕНА")

#ВЫВОДИМ ПОГРЕШНОСТЬ ВЫЧИСЛЕНИЙ ДЛЯ УСРЕДНЕННЫХ ПО СЕРИЯМ ЗНАЧЕНИЙ
for i in range(0, 4):
    middleValue = (SERIA1[i] + SERIA2[i] + SERIA3[i]) / 3
    print(f"ПОГРЕШНОСТЬ ВЫЧИСЛЕНИЙ УСРЕДНЕННЫХ ПО СЕРИЯМ ЗНАЧЕНИЙ ДЛЯ 10^{i+4} = {round_1(abs(funcValue - middleValue))}")


