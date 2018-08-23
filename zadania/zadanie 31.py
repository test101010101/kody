liczby = [ 4, 1, 2, 4, 5, 6, 7, 5, 4, 3, 2, 3, 4, 5, 4, 6]
i = 0

while True:
    podanaliczba = input("Zgadnij losową liczbę, naciśnij q aby skończyć")
    try:
        podanaliczba = int(podanaliczba)
    except(ValueError):
        podanaliczba = str(podanaliczba)
    if podanaliczba == liczby[i]:
        print ("Brawo, zgadłeś liczbę, spróbuj jeszcze raz!")
        i += 1
    elif podanaliczba == "q":
        "Program zostanie zakończony"
        break 
    else:
        print ("Tym razem ci sie nie udało, sprobuj jeszcze raz...")
        i += 1
    
    
        
