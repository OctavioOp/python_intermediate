import random

min1 = int(input('ingrese el numero menor: '))
max1 = int(input('ingrese numero mayor: '))


def radInt(min=0, max=100):
    minus = max - min
    if max > min and max > 0:
        num = round(random.random() * minus + min)
        return num
    elif min > max:
        return print('error valor maximo minimo')
    elif max < 0:
        return print('error valor maximo igual a 0')


print(radInt(min=min1, max=max1))


def radInt2(max=0, min=0):
    return round(random.random() * (max - min) + min)


def loto():
    carton = []
    while True:
        bolita = radInt2(1, 36)
        if bolita in carton:
            continue
        carton.append(bolita)
        if len(carton) == 6:
            break
    return carton
