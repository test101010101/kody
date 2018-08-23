import csv

movies = [["Top Gun", "Ocean's Eleven", "Report mniejszości"], ["Titanic", "Ostatni Jedi", "Incepcja"],["Pulp Fiction", "Człowiek w ogniu", "Seksmisja"]]

with open ("st.csv", "w") as f:
    write = csv.writer(f, delimiter=",")
    for movie_list in movies:
        write.writerow(movie_list)
        
