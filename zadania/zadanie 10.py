def f():
    global a 
    a = input("Podaj liczbę do podzielenia przez 2")
    a = int(a)
    a = a // 2
    
def g():
    global a
    a = a * 4
    print (a)

f()
g()
