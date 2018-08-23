text = input("Co zapisać w pliku?")
with open ("sst.txt", "w") as f:
    f.write(text)
    
