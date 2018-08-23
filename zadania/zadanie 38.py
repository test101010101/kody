import random

words = ["kot", "pies","chomik","koń","krowa","kura","indyk","kogut","świnia","słoń","żyrafa","tygrys","lew","mrówka","pająk","mysz","jaszczurka","żmija","wąż","zając","dzik","królik","wiewiórka","żaba",\
"sarna","jeleń","pantera","kuna","małpa","goryl","hipopotam","niedźwiedź", "krokodyl", "borsuk", "wilk", "lis", "fretka", "surykatka", "panda", "jeż",\
"leniwiec", "zebra", "kameleon", "łoś","lama", "jastrząb", "jaskółka","sowa", "wrona", "dzięcioł","papuga", "wieloryb", "delfin", "mors", "żółw", "bóbr", "foka","pingwin", "myszołów"]

word_from_list = words[random.randint(0,len(words))]

def hangman(word):
    wrong = 0
    stages = ["",
              "_______     ",
              "|           ",
              "|     |     ",
              "|     0     ",
              "|    /|\    ",
              "|    / \    ",
              "|           ",
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Gra w wisielca")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Odgadnij literę: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print ("\n".join(stages[0: e]))
        if "_" not in board:
            print("Wygrałeś")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages [0: wrong]))
        print("Przegrałeś! Miałeś odgadnąć: {}.".format(word))


hangman(word_from_list)
