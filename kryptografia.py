import random
import numpy as np
from random import randrange, getrandbits, randint

print("\n W python potęga to ** proszę tak wpisywać\n")
zad = int

while True:
    zad = int(input("wpisz numer zadania (1 = suma, 2 = xtime, 3 = iloczyn, 4 = odwrotnosc): "))


    def suma(a, b):
        c = hex(int(a, 16) ^ int(b, 16))
        return c

    def mnozenie(x, y):
        x = int(x, 16)
        y = int(y, 16)
        yp = y >> 1
        if not yp:
            return hex(x)
        if y & 1:
            return suma(mnozenie(xtime(hex(x)), hex(yp)), hex(x))
        else:
            return mnozenie(xtime(hex(x)), hex(yp))


    def xtime(a):
        a = int(a, 16)
        if a & (1 << 7):
            a = int(bin(a << 1).replace('0b', '')[-8:], 2)
            a ^= int('0x1B', 16)
        else:
            a = a << 1
        return hex(a)

    def odwrotnosc(x):
        x = hex(int(x, 16))
        y = x
        for i in range(253):
            y = mnozenie(x, y)
        if y == "0x0":
            return "undefined"
        else:
            return y[2:]

    if zad == 1:
        a = input("a = ")
        b = input("b = ")
        print(suma(a, b)[2:])

    if zad == 2:
        a = input("a = ")
        print(xtime(a)[2:])

    if zad == 3:
        a = input("a = ")
        b = input("b = ")
        print(mnozenie(a, b)[2:])

    if zad == 4:
        a = input("a = ")
        print(odwrotnosc(a))

