import random

print("\n W python potęga to ** proszę tak wpisywać\n")
zad = int


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


while True:
    zad = int(input("wpisz numer zadania: "))

    if zad == 1:
        p = eval(input("wpisz p: "))
        n = p
        def kat(p):
            a = random.randint(1, n - 1)
            b = random.randint(1, n - 1)
            if ((4*(a**3))+27*(b**2)) % p != 0:
                return ("a= ", a,"b= ", b)
            else: return kat(p)
        print (kat(p))

    if zad == 2:
        p = eval(input("wpisz p: "))
        a = eval(input("wpisz A: "))
        b = eval(input("wpisz B: "))

        def kat2(p):
            x = random.randint(1, p - 1)        #dajemy random x
            k = (x**3 + a*x + b)                #liczymy y
            if mod(k, (p-1)//2, p):             #sprawdzamy czy się nadaje
                y = mod(k, (p-1)//4, p)         #jeśli tak to mod
                return("x= ", x,"y= ", y)
            else: return kat2(p)                #jeśli nie to losujemy znowu
        print(kat2(p))


        def mod(be, e, m):
            if m == 1:
                return 0
            r = 1
            be = be % m
            while e > 0:
                if e % 2 == 1:
                    r = (r * be) % m
                e = e >> 1
                be = (be * be) % m
            return r

    if zad == 3:
        p = eval(input("wpisz p: "))
        a = eval(input("wpisz A: "))
        b = eval(input("wpisz B: "))
        x = eval(input("wpisz x: "))
        y = eval(input("wpisz y: "))


        def czy_punkt_nalezy(p, a, b, x, y):
            if (((x*x*x) + (a*x) + b) - (y * y)) % p == 0:
                return("TRUE")

            else: return("FALSE")
        print(czy_punkt_nalezy(p, a, b, x, y))

    if zad == 4:
        p = eval(input("wpisz p: "))
        x = eval(input("wpisz x: "))
        y = eval(input("wpisz y: "))
        print('x= ', x, 'y= ', p - y)

    if zad == 5:                            #nie ma przykładów :( zakładam, że nie będzie nieskończoności
        p = eval(input("wpisz p: "))
        a = eval(input("wpisz A: "))
        b = eval(input("wpisz B: "))
        x1 = eval(input("wpisz x1: "))
        y1 = eval(input("wpisz y1: "))
        x2 = eval(input("wpisz x2: "))
        y2 = eval(input("wpisz y2: "))
        if x1 == x2 and y1 == y2:
            o = odwrotnosc(2*y1, p)
            s = (3 * x1 * x1 + a) * o
        else:
            s = delta(y1, y2, x1, x2, p)
        x = s * s - x1 - x2 % p
        y = s * (x1 - x) - y1 % p


        print('x= ', x, 'y= ', y)













