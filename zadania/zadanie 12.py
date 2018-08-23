def f():
    """ Pobiera liczbę, którą chcemy podnieść do kwadratu, a następnie ją zwraca
    :input a: wpisujemy liczbę
    :int(a): konwersja do liczby całkowitej
    :a**2: obliczanie kwadratu liczby a
    :return: liczba a, czyli kwadrat liczby pobranej
    """
    a = input("wpisz liczbę, którą podniesiemy do kwadratu")
    a = int(a)
    a = a**2
    return a

def f():
    """ Pobiera wartośc typu str, i ją zwraca
    :input: pobiera wartość str
    :return: zwraca ją
    """
    string = input("Podaj łańcuch znaków, który mamy wyświetlić:")
    return (string)

def f(x, y, z, a=10, b=20):
    """ pobiera 3 wymagane parametry, mnoży je przez siebie,i je mnoży przez 2 parametramy domyślne
    :param x: parametr wymagany pierwszy
    :param y: parametr wymagany drugi
    :param z: parametr wymagany trzeci
    :param a: parametr domyślny pierwszy,10
    :param b: parametr domyślny drugi,20
    """
    return x * y * z * a * b

def f():
    """ Ustawia parametr globalny a, zmienia go w liczbę całkowitą, a następnie dzieli go przez 2
    :global a: działamy na globalnym a
    :input: pobiera wartość typu str
    :int(a): konwertuje wartość a typu str w wartość typu int
    :a//2: dzieli a przez 2
    """
    global a 
    a = input("Podaj liczbę do podzielenia przez 2")
    a = int(a)
    a = a // 2
def g():
    """pobiera paramter globalny a, mnoży go przez 4 i go podaje
    :global a: pobiera parametr globalny a
    global a
    a = a * 4
    print (a)
