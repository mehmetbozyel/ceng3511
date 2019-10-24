with open("kakuro_input.txt", "r") as kakuro:
    veri = kakuro.readline()
    veri = veri.strip("\n")
    veri = veri.split(", ")
    print(veri)
    veri = kakuro.readline()
    veri = veri.strip("\n")
    veri = veri.split(", ")
    print(veri)
