moyenne = float(input("Entrer la moyenne de l'eleve:"))
if(moyenne < 12 and moyenne > 10):
    print("Passable")
else:
    if(moyenne >= 12 and moyenne <14):
        print("Mention assez bien")
    else:
        if(moyenne >= 14 and moyenne <16):
            print("Bien")
        else:
            print("Merci")


moyenne = float(input("Entrer la moyenne de l'eleve:"))
if(moyenne < 12 and moyenne > 10):
    print("Passable")
elif(moyenne >= 12 and moyenne <14):
    print("Mention assez bien")
elif(moyenne >= 14 and moyenne <16):
    print("Bien")
else:
    print("Merci")

