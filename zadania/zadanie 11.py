def f(x):
    try:
        x = float(x)
        return (x)
    except ValueError:
        print("Złe dane wejściowe!")

c = f("aaaa")
print (c)
