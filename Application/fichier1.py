f = open("example.txt", "a")
for i in range(2):
    nom = input("Entrer le nom de l'étudiant " + str(i + 1) + ":")
    prenoms = input("Entrer le prenoms de l'étudiant " + str(i + 1)  + ":")
    nationnalité = input("Entrer la nationnalitéde l'étudiant "+ str(i + 1) + ":")
    note = input("Entrer la note de l'étudiant "+ str(i + 1) + ":")
    ligne = nom + "," + prenoms + "," + nationnalité + "," + note + "\n"
    f.writelines(ligne)
f.close()