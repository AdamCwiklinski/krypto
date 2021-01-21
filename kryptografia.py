import random
from random import randrange, getrandbits, randint

print("\n W python potęga to ** proszę tak wpisywać\n")
zad = int

while True:
    zad = int(input("wpisz numer zadania: "))


    def odwrotnosc(b, n):
        x = 0
        xx = 1
        while n != 0:
            i = b // n
            b, n = n, b - i * n
            xx, x = x, xx - i * x

        return xx


    def delta(y1, y2, x1, x2, p):
        return (y1 - y2 % odwrotnosc((x1 - x2), p))

    def z5(x1, x2, y1, y2, p):
        if x1 == x2 and y1 == y2:
            o = odwrotnosc(2 * y1, p)
            s = (3 * x1 * x1 + a) * o
        else:
            s = delta(y1, y2, x1, x2, p)
        x = s * s - x1 - x2 % p
        y = s * (x1 - x) - y1 % p
        return (x,y)


        def kat(p):
            a = random.randint(1, n - 1)
            b = random.randint(1, n - 1)
            if ((4 * (1 ** 3)) + 27 * (b ** 2)) % p != 0:
                return a, b
            else:
                return kat(p)
        a1, b1 = kat(k)

    if zad == 2:
        p = eval(input("p = "))
        a = eval(input("A = "))
        b = eval(input("B = "))
        x = eval(input("x = "))
        y = eval(input("y = "))
        n = eval(input("n = "))


        def kat(p):
            a = random.randint(1, n - 1)
            b = random.randint(1, n - 1)
            if ((4 * (1 ** 3)) + 27 * (b ** 2)) % p != 0:
                return a, b
            else:
                return kat(p)


        a1, b1 = kat(p)
        P = "({}, {})".format(x, y)
        x2 = x
        y2 = y

        xq, yq = z5(x, x,y,y, p)
        n = n // 2
        print(xq, " ", yq)

    if zad == 1:
        k = eval(input("k = "))
        n = k





































